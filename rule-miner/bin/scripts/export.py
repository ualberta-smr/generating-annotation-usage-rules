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
        exit(1)


    resp = requests.get(f"{backendUrl}/packages/{username}/confirmed")

    if resp.status_code == 200:
        # print(dumpJson(resp))
        # will need to save to a file
        out = f"{exportedRulesDir}/confirmed-{username}.json"
        with open(out, "w") as f:
            dumpJson(resp, f)
            print("Exported the confirmed rules to: " + out)
    else:
        print("Error occurred")
        print(f"Server returned with the status code: {resp.status_code}")
        print(dumpJson(resp))