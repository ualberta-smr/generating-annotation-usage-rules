import shutil
import subprocess
from common import createDirIfDoesNotExist, getEnv, getMostRecentUsername, move
import zipfile
import glob

if __name__ == "__main__":
    libSourcesDir       = "/pipeline/lib-sources"
    exportedRulesDir    = getEnv("EXPORT_DIR")
    detectorPluginDir   = "/pipeline/detector/violation-detector-maven-plugin"
    detectorLibDir      = "/pipeline/detector/violation-detection"
    detectorResourceDir = f"{detectorPluginDir}/src/main/resources/"
    currentUsername     = getMostRecentUsername()

    # zip all the jars into one zip file, and call it lib.zip
    jars = glob.glob(f"{libSourcesDir}/*.jar")
    with zipfile.ZipFile("/tmp/lib.zip", "w") as zipFile:
        for jar in jars:
            zipFile.write(jar, compress_type=zipfile.ZIP_DEFLATED)
    print("Zipped all the jar files into lib.zip")
    # copy confirmed rules file and rename it to rules.json

    shutil.copy(f"{exportedRulesDir}/confirmed-{currentUsername}.json", "/tmp/rules.json")

    # copy the zip and json files to /detector/violation-detector-maven-plugin/src/main/resources/
    move("/tmp/lib.zip", f"{detectorResourceDir}/lib.zip")
    move("/tmp/rules.json", f"{detectorResourceDir}/rules.json")

    # mvn clean install /detector/violation-detection               
    #                   /detector/violation-detector-maven-plugin
    installLibProcess   = subprocess.run(["mvn", "clean", "install", "-f", f"{detectorLibDir}/pom.xml"])
    if installLibProcess.returncode == 0:
        print("Successfully installed the violation-detection library")
    else:
        print("Installation of violation-detection library failed")
        exit(1)

    installPluginProcess = subprocess.run(["mvn", "clean", "package", "-f", f"{detectorPluginDir}/pom.xml"])
    if installPluginProcess.returncode == 0:
        print("Successfully built the violation-detector-maven-plugin plugin")
    else:
        print("Building the violation-detector-maven-plugin failed")
        exit(1)

    # copy the jar file to exports directory
    createDirIfDoesNotExist(f"{exportedRulesDir}/detector")
    move(f"{detectorPluginDir}/target/violation-detector-maven-plugin-jar-with-dependencies.jar", f"{exportedRulesDir}/detector/detector.jar")
    # create an install.sh script to install the jar file so that people can use it easily
    shutil.copy("/pipeline/bin/install-plugin.sh", f"{exportedRulesDir}/detector")
    
    print("Done!")
    print("Saved the jar file to '/pipeline/exports/detector' directory alongside installation script")