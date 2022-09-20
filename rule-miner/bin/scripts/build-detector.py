import shutil
import subprocess
import sys
from common import createDirIfDoesNotExist, extractParameterFromCommandLineArgs, getEnv, getMostRecentUsername, move
import zipfile
import glob
import os

def getConfirmedRulesFile():
    filename = extractParameterFromCommandLineArgs("--file")

    if filename and os.path.exists(filename):
        print(f"--file parameter has been provided, using the file: {filename}")
        return filename

    exportedRulesDir = getEnv("EXPORT_DIR")
    currentUsername  = getMostRecentUsername()
    if currentUsername:
        filename = f"{exportedRulesDir}/confirmed-{currentUsername}.json"
        if os.path.exists(filename):
            return filename
    
    print("Could not find a confirmed rules file. --file has not been provided")
    print("There is no valid username or a confirmed file associated with a valid username available")
    sys.exit(1)

if __name__ == "__main__":
    if extractParameterFromCommandLineArgs("--help", True):
        print("build-detector [options...]")
        print("options:")
        print("     1. --file [path]            - the path to the confirmed rules file")
        print("     2. --user [username]        - the username associated with the rule validation session")
        print("details:")
        print("--file and --user essentially help with the same thing - deciding which file to choose that contains the final confirmed rules")
        print("when both options are used, --file supersedes the --user option")
        print()
        sys.exit(0)

    libSourcesDir       = "/pipeline/lib-sources"
    exportedRulesDir    = getEnv("EXPORT_DIR")
    detectorPluginDir   = "/pipeline/detector/violation-detector-maven-plugin"
    detectorLibDir      = "/pipeline/detector/violation-detection"
    detectorResourceDir = f"{detectorPluginDir}/src/main/resources"

    # copy confirmed rules file and rename it to rules.json
    confirmedRulesFile = getConfirmedRulesFile()
    shutil.copy(confirmedRulesFile, "/tmp/rules.json")

    # zip all the jars into one zip file, and call it lib.zip
    jars = glob.glob(f"{libSourcesDir}/**/*.jar", recursive=True)
    if jars == []:
        print(f"No jar files were found in the {libSourcesDir} directory.")
        sys.exit(1)

    with zipfile.ZipFile("/tmp/lib.zip", "w") as zipFile:
        for jar in jars:
            zipFile.write(jar, compress_type=zipfile.ZIP_DEFLATED)
    print("Zipped all the jar files into lib.zip")

    # copy the zip and json files to /detector/violation-detector-maven-plugin/src/main/resources/
    move("/tmp/lib.zip", f"{detectorResourceDir}/lib.zip")
    move("/tmp/rules.json", f"{detectorResourceDir}/rules.json")

    
    # install the library so that we can use it while building the detector plugin
    installLibProcess   = subprocess.run(["mvn", "clean", "install", "-f", f"{detectorLibDir}/pom.xml"])
    if installLibProcess.returncode == 0:
        print("Successfully installed the violation-detection library")
    else:
        print("Installation of violation-detection library failed")
        sys.exit(1)

    # build the detector plugin
    installPluginProcess = subprocess.run(["mvn", "clean", "package", "-f", f"{detectorPluginDir}/pom.xml"])
    if installPluginProcess.returncode == 0:
        print("Successfully built the violation-detector-maven-plugin plugin")
    else:
        print("Building the violation-detector-maven-plugin failed")
        sys.exit(1)

    # copy the jar file to '/pipeline/exports/detector' directory
    createDirIfDoesNotExist(f"{exportedRulesDir}/detector")
    move(f"{detectorPluginDir}/target/violation-detector-maven-plugin-jar-with-dependencies.jar", f"{exportedRulesDir}/detector/detector.jar")
    # create an install.sh script to install the jar file so that people can use it easily
    shutil.copy("/pipeline/bin/install-plugin.sh", f"{exportedRulesDir}/detector")
    
    print("Done!")
    print("Saved the jar file to '/pipeline/exports/detector' directory alongside installation script")