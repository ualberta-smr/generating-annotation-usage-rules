import glob
import json
import requests
from randomname import get_name

if __name__ == '__main__':
    files = glob.glob('rules_*.json')

    if len(files) == 0:
        print("No rules file found. Try running: mine")
        exit(1)

    file_time = dict()

    for file in files:
        # remove 'rules_' and '.json' and only keep the timestamp
        timestamp = file[6:-5]
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
        f'http://backend:5000/packages?username={username}&packageName=MicroProfileRules', files=files)

    if resp.status_code == 200:
        print("==========================================================")
        print("Successfully loaded the mined candidate rules!")
        print("To start validating candidate rules, please head over to:")
        print("\thttp://localhost:8888")
        print(f"\tUsername: {username}")
        print("==========================================================")
        with open("/tmp/rvt_most_recent_login", "w") as f:
            f.write(username)
    else:
        print("==========================================================")
        print("Something went wrong!")
        print(f"Status code: {resp.status_code}")
        print("Error: ")
        print(resp.json())
        print("==========================================================")
