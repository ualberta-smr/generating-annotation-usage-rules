import glob
import json
import os
import sys
import requests
from randomname import get_name
from common import extractParameterFromCommandLineArgs, extractUserNameFromCommandLineArgs, getEnv, dumpJson

def getCandidateRulesFile():
    exportDir = getEnv("EXPORT_DIR")

    filename = extractParameterFromCommandLineArgs("--file")

    if filename and os.path.exists(filename):
        print(f"--file parameter has been provided, using the file: {filename}")
        return filename

    print("--file parameter has not been provided or the provided path does not exist. Trying to find the most recently produced candidate rules file")
    files = glob.glob(f'{exportDir}/candidate_rules_*.json')

    if len(files) == 0:
        print("No rules file found. Try running: mine")
        sys.exit(1)

    file_time = dict()

    # we will take the substring between prefix and suffix
    prefixLen = len(f'{exportDir}/candidate_rules_')
    suffixLen = len(".json")
    for file in files:
        # remove '{exportDir}/candidate_rules_' and '.json' and only keep the timestamp
        timestamp = file[prefixLen:-suffixLen]
        if timestamp.isnumeric():
            file_time[file] = int(timestamp)
        else:
            print("Ignoring file..." + file)

    if len(file_time) == 0:
        print("No rules file found. Try running: mine")
        sys.exit(1)

    return max(file_time, key=file_time.get)

def ensureBackendIsUp(backendUrl):
    try:
        requests.get(f'{backendUrl}')
    except requests.exceptions.ConnectionError:
        print("The backend server is not up yet. It may take some time for the backend and database to be fully-functional. Please try again")
        exit(2)

if __name__ == '__main__':
    if extractParameterFromCommandLineArgs("--help", True):
        print("validate [options...]")
        print("options:")
        print("     1. --file [path]            - the path to the candidate rules file. If none provided, it will select the most recent one")
        print(f"                                   based on the timestamp of the file located in {getEnv('EXPORT_DIR')}")
        print("     2. --user [username]        - the username associated with the rule validation session. The final file will contain this username.")
        print(f"                                   If none provided, it will use the one located in {getEnv('MOST_RECENT_LOGIN_PATH')}")
        print()
        sys.exit(0)
    
    frontendPort        = int(getEnv("FRONTEND_URL").split(":")[2])
    backendUrl          = getEnv("BACKEND_URL")
    mostRecentLoginFile = getEnv("MOST_RECENT_LOGIN_PATH")

    ensureBackendIsUp(backendUrl)

    filename = getCandidateRulesFile()
    print("Using the following rules file for the validation: " + filename)

    with open(filename) as f:
        rules = json.load(f)
        if len(rules) == 0:
            print(f"Warning: Loaded candidate rules file is empty. Stopping the execution")
            sys.exit(1)
        # order the ids
        # each rule will have an id, that starts from 1
        # and ends in N which is the number of all available rules
        id = 1
        for aRule in rules:
            aRule["id"] = id
            id += 1
            # these two fields are unnecessary for RVT
            del aRule["label"]
            del aRule["sameAs"]
        
        files = {
            'rulesFile': ('file', json.dumps(rules), 'application/json')
        }

    # generate a random name
    username = extractUserNameFromCommandLineArgs()
    if username is None:
        print("No username has been provided, generating a random one...")
        username = get_name()

    resp = requests.post(
        f'{backendUrl}/packages?username={username}&packageName=MicroProfileRules', files=files)

    print("==========================================================")
    if resp.status_code == 200:
        # saving the most recent username
        # because the 'export-rules' command might need it
        with open(mostRecentLoginFile, "w") as f:
            f.write(username)
        print("Successfully loaded the mined candidate rules!")
        print("To start validating candidate rules, please head over to:")
        print(f"\thttp://localhost:{frontendPort}")
        print(f"\tUsername: {username}")
    else:
        print("Something went wrong!")
        print(f"Status code: {resp.status_code}")
        print("Error: ")
        print(dumpJson(resp))
    print("==========================================================")
