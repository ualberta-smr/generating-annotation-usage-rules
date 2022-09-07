import requests
import json

if __name__ == "__main__":
    try:
        # this is where the most recent login is stored
        with open("/tmp/rvt_most_recent_login") as f:
            username = f.read().strip()
    except Exception as e:
        print(e.args[0])
        exit(1)

    resp = requests.get(f"http://backend:5000/packages/{username}/confirmed")

    print(json.dumps(resp.json(), indent=4))