import os
import json
import shutil
from pathlib import Path
import sys


def getEnv(key):
    res = os.getenv(key)
    if res is None:
        raise Exception(
            f"The environment variable '{key}' should be set to run the 'export-rules' command")
    return res


def dumpJson(response, fileHandle=None):
    if fileHandle:
        # returns None
        return json.dump(response.json(), fileHandle, indent=4)
    else:
        # returns string
        return json.dumps(response.json(), indent=4)

def extractUserNameFromCommandLineArgs():
    try:
        ix = sys.argv.index("--user")
        if ix + 1 < len(sys.argv):
            return sys.argv[ix + 1]
    except:
        return None


def getMostRecentUsername():
    username = extractUserNameFromCommandLineArgs()
    if username:
        return username

    with open(getEnv("MOST_RECENT_LOGIN_PATH")) as f:
        username = f.read().strip()
        if not username or len(username) == 0:
            raise Exception("No username has been provided and the most recent username is empty")
        return username


def move(src, dest):
    if os.path.isfile(dest):
        os.remove(dest)
    shutil.move(src, dest)

def ensureFileExists(src):
    if os.path.isfile(src):
        raise FileNotFoundError(src)

def createDirIfDoesNotExist(dir):
    Path(dir).mkdir(parents=True, exist_ok=True)
