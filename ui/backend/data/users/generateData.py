import json
from random import randint, shuffle

USER_MAPPING = {
    "mansur": 1,
    "ajay": 2,
    "user1": 3,
    "user2": 4,
    "user3": 5,
}

def removeKey(obj, key):
    if key in obj:
        del obj[key]

with open("base.json") as base:
    data = json.load(base)

    for username, user_id in USER_MAPPING.items():
        size = randint(50, len(data))
        shuffle(data)
        newData = data[:size]

        for i in range(size):
            newData[i]["id"] = i + 1
            removeKey(newData[i], "label")
            removeKey(newData[i], "distance")
            removeKey(newData[i], "distanceComments")
            removeKey(newData[i], "sameAs")
        
        with open(f"data_{username}.json", "w") as file:
            file.write(json.dumps(newData))