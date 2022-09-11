import glob
import json
import requests
from randomname import get_name
from common import getEnv, dumpJson

if __name__ == '__main__':
    frontendPort        = int(getEnv("FRONTEND_URL").split(":")[2])
    backendUrl          = getEnv("BACKEND_URL")
    mostRecentLoginFile = getEnv("MOST_RECENT_LOGIN_PATH")
    exportDir           = getEnv("EXPORT_DIR")

    files = glob.glob(f'{exportDir}/candidate_rules_*.json')

    if len(files) == 0:
        print("No rules file found. Try running: mine")
        exit(1)

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
        exit(1)

    filename = max(file_time, key=file_time.get)
    print("Using the following rules file for the validation: " + filename)

    with open(filename, 'r') as f:
        rules = json.load(f)
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
