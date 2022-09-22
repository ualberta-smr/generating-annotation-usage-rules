import json
import sys
import requests
from common import getEnv, dumpJson, getMostRecentUsername

if __name__ == "__main__":
    backendUrl          = getEnv("BACKEND_URL")
    exportedRulesDir    = getEnv("EXPORT_DIR")

    try:
        # this is where the most recent login is stored
        username = getMostRecentUsername()
    except Exception as e:
        print("Error occurred while trying to access the most recent username")
        print("Error: "+ str(e.args[0]))
        sys.exit(1)

    resp = requests.get(f"{backendUrl}/packages/{username}/confirmed")

    if resp.status_code == 200:
        rules = resp.json()
        if len(rules["rules"]) == 0:
            print(f"There are no confirmed rules for the user: {username}")
            exit(1)
        # add generic id for each rule: Rule-#    
        for i, rule in enumerate(rules["rules"]):
            rule["id"] = f"Rule-{i + 1}"

        out = f"{exportedRulesDir}/confirmed-{username}.json"
        with open(out, "w") as f:
            json.dump(rules, f, indent=4)
            print("Exported the confirmed rules to: " + out)
    else:
        print("Error occurred")
        print(f"Server returned with the status code: {resp.status_code}")
        print(dumpJson(resp))