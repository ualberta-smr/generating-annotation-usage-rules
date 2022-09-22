# Documentation

# Table of contents

- [Overall workflow](#overall-workflow)
- [Configuration](#configuration)
- [Building and running](#building-and-running)
- [Mining](#mining)
- [Validation](#validation)
- [Export](#export)
- [Building the misuse detector](#building-the-misuse-detector)
- [Installing and running the detector](#installing-and-running-the-detector)
- [Downloading projects and jar files](#downloading-projects-and-jar-files)
    - [Downloading JARS](#downloading-jars)
    - [Cloning projects](#cloning-projects)


## Overall workflow

To be able to use the tool, we first need to configure it and make sure we provide all the necessary input. Next, we can build, and then run the tool. Once inside of the container, we need to mine the rules and then validate them. Once the validation is complete, we need to export the confirmed rules, and finally build the detector that is equipped with the confirmed rules.

## Configuration

To be able to mine annotation usage rules, the tool requires three things:
- a set of input Java projects to mine the rules from
- a set of JAR files for resolving the types of imported classes, annotations, etc. 
    - *if not provided, the miner uses a heuristic which may not always produce accurate results*
- [`configuration.json`](./config/configuration.json) file that specifies what APIs we want to mine rules for

The first two parameters can be provided through mounting existing directories to their respective volumes mentioned in the [`docker-compose.yml`](./docker-compose.yml) file. We currently expose three volumes:

- `mining-sources`  - represents the directory where the input Java projects will reside in.
- `lib-sources`     - represents the directory where the JAR files will reside in.
- `exports`         - represents the directory where the exported artifacts (candidate rules, confirmed rules, the detector, etc.) will reside in. 

By default, these volumes are mounted to the directories with the same name in your host machine in the root of this project's directory. See the `miner.volumes` section in the [`docker-compose.yml`](./docker-compose.yml) file if you want to change any default directory.

While you can certainly populate these input directories yourself, we also provide tools to download the input Java projects (from GitHub) and JAR files (from Maven Central). See [Downloading Projects and JAR files](#downloading-projects-and-jar-files) section.

[`configuration.json`](./config/configuration.json) file contains the necessary information about the APIs we are interested in mining. Example file:

```json
{
    "api": {
        "prefixes": [
            "org.eclipse.microprofile",
            "javax",
            "jakarta"
        ],
        "subApi": {
            "prefixes": [
                "org.eclipse.microprofile.config",
                "org.eclipse.microprofile.faulttolerance",
                "org.eclipse.microprofile.graphql",
                "org.eclipse.microprofile.health",
                "org.eclipse.microprofile.jwt",
                "org.eclipse.microprofile.metrics",
                "org.eclipse.microprofile.openapi",
                "org.eclipse.microprofile.opentracing",
                "org.eclipse.microprofile.reactive",
                "org.eclipse.microprofile.rest",
                "org.eclipse.microprofile.auth"
            ]
        }
    }
}
```

We simply need two types of `prefixes` for the configuration:

- `api#prefixes` is used to make sure the provided rules contain at least one annotation that belong to any of these namespaces. 
- `api#subApi#prefixes` is used to group the annotation usages based on the sub-APIs (i.e., packages), and perform the mining for each sub-API individually. The mining parameters are automatically configured according to the size of each group. This improves the quality of the mined rules.

## Building and running

Once configuration is done, build and run the application. We can build the application using [`build.sh`](./build.sh) command. Once the project is successfully built, we can run it using [`run.sh`](./run.sh) command. A successful execution will land you in the bash shell.

```shell

your-host-machine> ./build.sh && ./run.sh
# some build related output
# ...
========================================================================
This tool allows you to mine candidate annotation usage rules 
from the target projects located in /pipeline/mining-sources.
Once you mine candidate rules, you can review and validate them 
using the Rule Validation Tool (RVT). Confirmed rules can be exported 
to be used for misuse detection.

Available commands:
	 mine                  - Mines candidate rules from target projects located in /pipeline/mining-sources
	 validate              - Uploads the mined candidate rules into the RVT for validation
	 export-rules          - Exports the validated correct rules from RVT
	 build-detector        - Builds the misuse detector Maven plugin jar file, and provides installation directions
	 download-jars         - Downloads the required jar files mentioned in /pipeline/config/configuration.json file
	 clone-projects        - Clones the projects mentioned in the input file into /pipeline/mining-sources directory
	 info                  - Shows information about the available commands
pipeline> 
```

By default, every time you run the container, the `info` command is automatically run to show the available commands. You can obviously use the `info` command at any point in time to get the same information.

We have 7 commands each performing different tasks. We now will describe each command individually.

## Mining

Assuming that we have configured the `mining-sources` and `lib-sources` accurately (meaning that they contain the input Java projects, and JAR files), to start the mining process, all we need to do is to issue the `mine` command. That's it! Once the mining process is done, it will save the candidate rules to the `/pipeline/exports` directory (the name template is `candidate_rules_{current_milliseconds}.json`). 

Note. [`mine`](./rule-miner/bin/mine) command is a wrapper around the miner which is a runnable fat-JAR file. If you want to provide custom configuration values, you can certainly run the miner jar file.

## Validation

Once the candidate rules are mined, we can move on to the validation. To perform the validation, we need to upload the candidate rules to our Rule Validation Tool (RVT). To do this, we simply need to issue the `validate` command. This command will upload the candidate rules to RVT and provide a random username for accessing those rules. Example execution:
```
pipeline> validate

Using the following rules file for the validation: /pipeline/exports/candidate_rules_1663128572285.json
No username has been provided, generating a random one...
==========================================================
Successfully loaded the mined candidate rules!
To start validating candidate rules, please head over to:
	http://localhost:8888
	Username: magnetic-gallery
==========================================================
```

You can also provide a custom username using `--user USERNAME` option:

```
pipeline> validate --user microprofile-rules
```

All you have to do is to put the username in the login field in the RVT login page and hit Enter.

<p align="center">
  <img src="./assets/1_login_landing_page.png" width="80%" />
</p>

To learn more about how to use RVT and its domain-specific language, please head over to [tutorial](./ui/tutorial/README.md).

By default, the `validate` command picks the most recent candidate rules file based on the timestamp (milliseconds) provided in the name of the file. However, if we want to specify a specific file, we can do that using the `--file FILEPATH` command as follows:

```shell
pipeline> validate --file /pipeline/examples/candidate_rules_example.json
```

**Note. ** The `validate` command saves the username (provided or generated) to `/tmp/rvt_most_recent_login` file in the container. This allows us to call the `export-rules` and `build-detector` commands (both explained next) without specifying the user, because both of these commands check the `/tmp/rvt_most_recent_login` file if no user is provided.

## Export

Once the validation is complete (which does not equate to validating all the candidate rules necessarily), we can export the confirmed rules from RVT. To do this, we can issue the `export-rules` command. Example command:

```
pipeline> export-rules 

Exported the confirmed rules to: /pipeline/exports/confirmed-magnetic-gallery.json
```

By default, if no user is provided, `export-rules` takes the username from `/tmp/rvt_most_recent_login` file which is set by the `validate` command (as described above). However, since `/tmp/rvt_most_recent_login` is a temporary file, if we want to export rules for another username (or if we have restarted the container), we can supply a custom username as follows: 

```shell
pipeline> export-rules --user microprofile-rules

Exported the confirmed rules to: /pipeline/exports/confirmed-microprofile-rules.json
```

The `export-rules` command saves the confirmed rules to the `exports` directory with the name `confirmed-{username}.json`. 

## Building the misuse detector

We can use the exported confirmed rules for building a misuse detector. To build the misuse detector, we only need to issue the `build-detector` command which will package our misuse detector Maven plugin with the exported rules and the jar files required for type resolving, into a single jar file. This jar file, alongside a shell script to install it will be available in `/pipeline/exports/detector/` directory. You can issue the install command from your host machine or any other device that has Java and Maven installed.

Similar to the `export-rules` command, you can also supply a custom username to the `build-detector` command using `--user USERNAME` option. Since the confirmed rules contain the username that they belong to, this option allows us to pick anything other than the most recent username.

By default, the `build-detector` command uses the confirmed rules file associated with the provided or most recent username. However, if we want to provide a specific file, we can use the `--file FILEPATH` command as follows:

```shell
pipeline> build-detector --file /pipeline/examples/confirmed_rules_example.json
```

## Installing and running the detector

To install the detector, all we need to do is to run the provided installation script.

Since the detector is a Maven plugin, we need to run it in a Maven project. A very simple example:

```
# mvn ca.ualberta:violation-detector-maven-plugin:scan
```

To learn more about running the detector, please see the **How to use the plugin** section in [the following tutorial](./violation-detector/README.md#how-to-use-the-plugin).

## Downloading projects and jar files

Our tool provides commands for downloading jar files and cloning the target projects from GitHub. 

### Downloading JARs 

To download the jars, you can add an array called `"jarFiles"` to `configuration.json` file where each element in the array represents a jar file that will be downloaded from Maven Central. The format for each entry is `groupId:artifactId:version`. The [configuration.json](./config/configuration.json) file we have provided contains an example.

Once the *configuration.json* file contains all the entries, you can issue the command `download-jars` command. If you have already mounted an existing directory to `lib-sources` volume, please be aware that the `download-jars` command will not delete or re-download existing jar files. Example command:

```shell
pipeline> download-jars # no parameter required
```

### Cloning projects

To clone target projects from GitHub, you can use `clone-projects` command which takes a path to a file where all the projects are mentioned. Check out an example file [here](./examples/example_projects.txt). The format for an entry is that the first line is the GitHub link, the next line may have a commit hash (will checkout the master/main branch if none specified), and finally "--" (dashes) are used as the separator. Putting any file in the [`config`](./config/) directory will result in that file being copied to the container. Finally, the projects will be downloaded to `/pipeline/mining-sources` directory in the container. Example command: 

```shell
pipeline> clone-projects --file /pipeline/config/projects.txt
```
