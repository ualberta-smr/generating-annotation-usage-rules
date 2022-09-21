# Pipeline for producing annotation usage rules  

This tool allows mining candidate annotation usage rules from target projects, validating these candidate rules, and finally generating a misuse detector in the form of a Maven plugin.

# Requirements

- Docker (tested on version 20)
    - The build files make use of [BuildKit](https://docs.docker.com/develop/develop-images/build_enhancements/) for caching purposes which were introduced in version 18.09. This means that the minimum Docker version required is 18.09.
- Docker Compose (tested on version 1.25)
- The following ports need to be free to make sure the application is running correctly:
    - 3306 - mysql
    - 5000 - backend
    - 8000 - ui tutorial
    - 8888 - ui

# Quick start

The pipeline has three major steps (i.e. mining, validating, creating the misuse detector) and there are commands available to perform each of these steps, and some other auxillary commands. In this section, we will quickly demonstrate each step so that the overall flow will be clearer.

## Building and running

To be able to use the pipeline, we need to build it first, and then run it. We can use [`build.sh`](./build.sh) and [`run.sh`](./run.sh) commands to achieve this as follows:

```shell
your-host-machine> ./build.sh && ./run.sh
# some build related output
# ...
========================================================================
This tool allows you to mine candidate annotation usage rules 
from the target projects located in ''.
Once you mine candidate rules, you can review and validate them 
using the Rule Validation Tool (RVT). Confirmed rules can be exported 
to be used for misuse detection.

Available commands:
	 mine                  - Mines candidate rules from target projects located in 
	 validate              - Uploads the mined candidate rules into the RVT for validation
	 export-rules          - Exports the validated correct rules from RVT
	 build-detector        - Builds the misuse detector Maven plugin jar file, and provides installation directions
	 download-jars         - Downloads the required jar files mentioned in  file
	 clone-projects        - Clones the projects mentioned in the input file into  directory
	 info                  - Shows information about the available commands
pipeline> 
```

A successful execution should land you in the bash shell, and information about all the available commands should be printed. Now the pipeline is ready!

## Mining

We will explain the mining step in detail in the mining section, but now we will quickly demonstrate how it works. To be able to mine candidate annotation usage rules (a.k.a. _candidate rules_), we need two input: 
    
1. a set of Java projects that we will use for mining
2. a set of JAR files for resolving the types that we are interested in

You can provide your own set of projects as well, but for the purpose of this demo, we will clone some predefined MicroProfile projects. To do this, please issue the following command:
```shell
pipeline> clone-projects --file /pipeline/examples/example_projects.txt
```

This will download all the projects defined in the [example_projects.txt](./examples/example_projects.txt) file into `/pipeline/mining-sources` directory. 

Next, we need to download the JAR files. To do this, please issue the following command:

```shell
pipeline> download-jars
```

This will download all the JAR files mentioned in the [`configuration.json`](./config/configuration.json) file into the `/pipeline/lib-sources` directory.

Now, we are ready to mine! To mine candidate rules, we can simply use the following command:

```shell
pipeline> mine
```

The mining process might take a while, which is why we have provide [an example output file](./examples/candidate_rules_example.json) that can be used in the validation process next.

## Validation

The next step after mining is to validate the candidate annotation usage rules. Usually, once the mining step is done, it is enough to issue the `validate` command to use the newly produced candidate rules for validation. However, in this section, we will use a predefined file to speedup the process. Issue the following command:

```shell
pipeline> validate --file /pipeline/examples/candidate_rules_example.json
Using the following rules file for the validation: /pipeline/examples/candidate_rules_example.json
No username has been provided, generating a random one...
==========================================================
Successfully loaded the mined candidate rules!
To start validating candidate rules, please head over to:
	http://localhost:8888
	Username: magnetic-gallery
==========================================================
```

Now, all you need to do is to go to `http://localhost:8888` and log in with the provided username, and start validating the candidate rules. The landing page will look something like this:

<p align="center">
  <img src="./assets/1_login_landing_page.png" width="90%" />
</p>

Once you're done with validation, you can simply close the browser tab.

## Building the detector

Once the validation is done, we can move on to building the detector which consists of two steps. 

1. Exporting the confirmed rules
2. Building the detector

Please note that if you have skipped the mining step entirely, and have not yet downloaded the jar files, please issue the following command to do it, as those jars are required for building the detector.

```shell
pipeline> download-jars
```

To perform both, simply run the command:

```shell
pipeline> export-rules && build-detector
```

However, if we simply want to build the detector from some predefined confirmed rules, issue the following command:

```shell
pipeline> build-detector --file /pipeline/examples/confirmed_rules_example.json
```

After a successful execution, please head over to `/pipeline/exports/detector` directory where you'll find `install-plugin.sh` alongside a JAR file of the detector. The `/pipeline/exports` directory is a volume, and by default it is mounted to a directory called `exports` in the project root in the host machine. You can try installing the detector using the provided script in your host machine.

You can also install the plugin within the pipeline and test it on a dummy project. To do it, you need to first install the plugin:

```shell
pipeline> pwd
/pipeline/exports/detector
pipeline> ./install-plugin.sh
# it will install the plugin
```

and then go to the dummy project directory, and issue the scanning task

```shell
pipeline> cd /pipeline/examples/example_project
pipeline> mvn ca.ualberta:violation-detector-maven-plugin:scan
```

After a successful execution, it should print out the misuses of "Rule-1".

# Getting started

### Configuration

To be able to mine annotation usage rules, the tool requires three things:
- target projects to mine the rules from
- jar files for resolving the types of imported classes, annotations, etc. If not provided, it falls back to a heuristic which may not always produce accurate results
- `configuration.json` file that specifies what APIs we want to mine rules for

The first two parameters can be provided through mounting existing directories to provided volumes in the [`docker-compose.yml`](./docker-compose.yml) file (see `volumes` section in the `miner` service). Additionally, we also provide means to download the target projects and jar files. See [this section](#downloading-projects-and-jar-files).

`configuration.json` file contains the necessary information about the APIs we are interested in mining. Example file:

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

- `api#prefixes` is used to make sure the provided rules only contain classes/annotations that belong to these namespaces. 
- `api#subApi#prefixes` is used to group the annotation usages based on the sub-APIs, and perform the mining for each sub-API individually where mining parameters are automatically configured according to the size of each group.

### Building and running

Once configuration is done, build and run the application. We can build the application using [`build.sh`](./build.sh) command. Once the project is successfully built, we can run it using [`run.sh`](./run.sh) command. A successful execution will land you in the `bash`.

```
bash5-1# 
```

You can use the `info` command to get more information.

```
bash-5.1# info

This tool allows you to mine candidate annotation usage rules 
from the target projects located in '/pipeline/mining-sources'.
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
```

We have 7 commands each performing different tasks. We now will describe each command individually.

### Mining

Assuming that we have configured the `mining-sources` and `lib-sources` accurately, to start the mining process, all we need to do is to issue the `mine` command. That's it! Once the mining process is done, it will save the candidate rules to the `/pipeline/exports` directory (the name template is `candidate_rules_{current_milliseconds}.json`). 

### Validation

Once the candidate rules are mined, we can move on to the validation. To perform the validation, we need to upload the candidate rules to our Rule Validation Tool (RVT). To do this, we simply need to issue the `validate` command. This command will upload the candidate rules to RVT and provide a random username for accessing those rules. Example execution:
```
bash-5.1# validate
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
bash-5.1# validate --user microprofile-rules
```

All you have to do is to put the username in the login field in the RVT login page and hit Enter.

<p align="center">
  <img src="./assets/1_login_landing_page.png" width="90%" />
</p>

To learn more about how to use RVT and its domain-specific language, please head over to [tutorial](./ui/tutorial/README.md).

**Note.** The `validate` command picks the most recent candidate rules file based on the timestamp (milliseconds) provided in the name of the file.

### Export

Once the validation is complete (which does not equate to validating all the candidate rules necessarily), we can export the confirmed rules from RVT. To do this, we can issue the `export-rules` command. Example command:

```
bash-5.1# export-rules 
Exported the confirmed rules to: /pipeline/exports/confirmed-magnetic-gallery.json
```

**Note.** The `validate` command saves the provided or the generated username to `/tmp/rvt_most_recent_login` file which is the reason why we do not need to supply the username to the `export-rules` command after we run `validate`. However, since `/tmp/rvt_most_recent_login` is a temporary file, if we want to export rules for another username (or if we have restarted the container), we can supply a custom username as follows: `export-rules --user microprofile-rules`.

### Building the misuse detector

We can use the exported confirmed rules for building a misuse detector. To build the misuse detector, we only need to issue the `build-detector` command which will package our misuse detector Maven plugin with the exported rules and the jar files required for type resolving into a single jar file. This jar file, alongside a Shell script to install it will be available in `/pipeline/exports/detector/` directory. You can issue the install command from your host machine or any other device that has Java and Maven installed.

**Note.** Similar to the `validate` and `export-rules` commands, you can also supply a custom username to the `build-detector` command using `--user USERNAME` option. Since the confirmed rules contain the username that they belong to, this option allows us to pick anything other than the most recent username.

### Running the detector

Since the detector is a Maven plugin, we need to run it in a project where a `pom.xml` is present. A very simple example:

```
# mvn ca.ualberta:violation-detector-maven-plugin:scan
```

To learn more about running the detector, please see the **How to use the plugin** section in [the following tutorial](./violation-detector/README.md#how-to-use-the-plugin).

### Downloading projects and jar files

Our tool provides two commands for downloading jar files, and cloning the target projects from GitHub. 

- **Downloading JARs**. To download the jars, you can add an array called `"jarFiles"` to `configuration.json` file where each element in the array represents a jar file that will be downloaded from Maven Central. The format for each entry is `groupId:artifactId:version`. Once the configuration.json file contains all the entries, you can issue the command `download-jars` command. If you have already mounted an existing directory to `lib-sources` volume, please be aware that the `download-jars` command will not delete or re-download existing jar files. Example command:
```shell
bash-5.1# download-jars # no parameter required
```

- **Cloning projects**. To clone target projects from GitHub, you can use `clone-projects` command which takes a path to a file where all the projects are mentioned. Check out an example file [here](./config/projects.txt). The format for an entry is that the first line is the GitHub link, the next line may have a commit hash (will checkout the master/main branch if none specified), and finally "--" (dashes) are used as the separator. Putting any file in the [`config`](./config/) directory will result in that file being copied to the container. Finally, the projects will be downloaded to `/pipeline/mining-sources` directory in the container. Example command: 
```shell
bash-5.1# clone-projects /pipeline/config/projects.txt
```
