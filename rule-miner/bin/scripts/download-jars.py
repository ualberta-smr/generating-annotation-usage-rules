from glob import glob
import traceback
from typing import List
from common import getEnv
import json
from dataclasses import dataclass
import urllib.request as urlReq

@dataclass
class JarDependency:
    groupId: str
    artifactId: str
    version: str
    downloadUrl: str
    fileName: str

    def getFullReference(self):
        return f"{self.groupId}:{self.artifactId}:{self.version}"

def createMvnRepositoryDownloadUrl(groupId: str, artifactId, version):
    groupId = groupId.replace(".", "/")
    return f"https://repo.maven.apache.org/maven2/{groupId}/{artifactId}/{version}/{artifactId}-{version}.jar", f"{artifactId}-{version}.jar"


def getListOfJarsToDownload(jarFilesArray) -> List[JarDependency]:
    fullPaths = []
    for jarDef in jarFilesArray:
        # e.g., "org.eclipse.microprofile.config:microprofile-config-api:3.0.1"
        #       "groupId                        :artifactId             :version"
        pieces = jarDef.split(":")
        if len(pieces) != 3:
            print(f"ERR! Incorrect format in {jarDef}")
            exit(1)
        
        groupId, artifactId, version = pieces
        downloadUrl, fileName = createMvnRepositoryDownloadUrl(groupId, artifactId, version)

        fullPaths.append(JarDependency(groupId, artifactId, version, downloadUrl, fileName))
    
    return fullPaths

def getExistingJars():
    jarsDir = getEnv("JARS_DIR")
    files = []
    for file in glob(f"{jarsDir}/**/*.jar", recursive=True):
        jarFileName = file.split("/")[-1]
        files.append(jarFileName)
    return files

if __name__ == "__main__":
    configPath  = getEnv("CONFIG_JSON_PATH")
    jarsDir     = getEnv("JARS_DIR")

    with open(configPath) as confFile:
        config = json.load(confFile)
        if "jarFiles" not in config:
            print(f"{configPath} file is missing 'jarFiles' array that is used to specify the dependencies that need to be downloaded")
            exit(1)
        
        jarFiles = config["jarFiles"]

        if len(jarFiles) == 0:
            print(f"'jarFiles' array in {configPath} is empty. Nothing to download. Exiting...")
            exit(0)
    
    jarDependencies = getListOfJarsToDownload(jarFiles)
    existingJars = getExistingJars()
    
    for e in list(filter(lambda x: x.fileName in existingJars, jarDependencies)):
        print(f"'{e.getFullReference()}' already exists in {jarsDir}. Skipping...")
        jarDependencies.remove(e)

    if len(jarDependencies) == 0:
        print("Jar files have already downloaded. Nothing to download. Exiting...")
        exit(0)
    
    size = len(jarDependencies)
    for i, jd in enumerate(jarDependencies):
        try:
            path, message = urlReq.urlretrieve(jd.downloadUrl, f"{jarsDir}/{jd.fileName}")
            print(f"[{i + 1}/{size}] Downloaded: {jd.downloadUrl}")
        except Exception as e:
            print(f"[{i + 1}/{size}] Could not download: {jd.getFullReference()}")
            traceback.print_stack()

    print("Done!")