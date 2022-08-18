# Violation Detector

To get started, you need to build and install both projects. You can achieve this as follows:

```shell
cd violation-detection/
mvn clean install

cd violation-detector-maven-plugin/
mvn clean install
```

Once the install process succeeds, you can use the plugin to find misuses.

## How to use the plugin

1) Without adding anything to the `pom.xml`, simply running `mvn ca.ualberta:violation-detector-maven-plugin:scan` triggers the scanning. Users can configure these parameters:
- **includes** - to only include certain files. Follows Ant-style patterns. Default: all Java files in the **targetDirectory**
- **excludes** - to exclude certain files. Follows Ant-style patterns. Default: all non-Java files in the **targetDirectory**
- **targetDirectory** - the directory that gets scanned. Default target directory is `${basedir}/src/main/java` which means that the `test` folder is not scanned. 
- **failOnViolation** - if it is set to `true`, any found violation will fail the build. Default is `false`

```shell
mvn ca.ualberta:violation-detector-maven-plugin:scan \
       -Dincludes="COMMA_SEPARATED_PATTERNS" \
       -Dexcludes="COMMA_SEPARATED_PATTERNS" \
       -DfailOnViolation="FAIL_ON_VIOLATION" \
       -DtargetDirectory="TARGET_DIRECTORY"
```

2) If we want to put our config into the `pom.xml`, then adding the following to the `pom.xml` works.

```xml
<build>
    <plugins>
        <plugin>
            <groupId>ca.ualberta</groupId>
            <artifactId>violation-detector-maven-plugin</artifactId>
            <version>1.0</version>
            <configuration>
                <!-- none of these parameters are required, and they have default values -->
                <!-- default value is **\/*.java basically all java files -->
                <includes>${COMMA_SEPARATED_PATTERNS}</includes>
                <!-- no default value -->
                <excludes>${COMMA_SEPARATED_PATTERNS}</excludes>
                <!-- default value is ${basedir}/src/main/java -->
                <targetDirectory>${TARGET_DIRECTORY}</targetDirectory>
                <!-- default value is false -->
                <failOnViolation>${FAIL_ON_VIOLATION}</failOnViolation>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>scan</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```
and then doing one of these triggers the scan:
- `mvn verify` (because plugin's default lifecycle phase is Verify)
- `mvn violation-detector:scan`

## Changing existing rules

The building process packages the rules file inside the `violation-detector` jar as well. Thus simply changing the contents of the rules file before building will result in new rules being used instead of the old ones. By default, the tool picks up the [`rules.json` file](./violation-detector-maven-plugin/src/main/resources/rules.json) which is loaded by the [`DefaultRuleProvider`](./violation-detector-maven-plugin/src/main/java/ca/ualberta/DefaultRuleProvider.java) class.