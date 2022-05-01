from typing import Dict, List

from fastapi import Response
from .models import User
from sqlalchemy.orm import Session


# username => user_id
USER_MAPPING = {
    # dummy data
    "mansur": 1,
    "ajay": 2,
    "user1": 3,
    "user2": 4,
    "user3": 5,
    # experiment subjects
    "P5": 6,
    "P1": 7,
    "P3": 8,
    "P6": 9,
    "P2": 10,
    "P4": 11
}

# user_id => package_info
USER_PACKAGE_MAPPING = {
    1: {"file": "./data/users/data_mansur.json", "package_id": 1},
    2: {"file": "./data/target_set.json", "package_id": 2},
    3: {"file": "./data/users/data_user1.json", "package_id": 3},
    4: {"file": "./data/users/data_user2.json", "package_id": 4},
    5: {"file": "./data/target_set.json", "package_id": 5},


    6: {"file": "./data/experiment_data/P5.json", "package_id": 6},
    7: {"file": "./data/experiment_data/P1.json", "package_id": 7},
    8: {"file": "./data/experiment_data/P3.json", "package_id": 8},
    9: {"file": "./data/experiment_data/P6.json", "package_id": 9},
    10: {"file": "./data/experiment_data/P2.json", "package_id": 10},
    11: {"file": "./data/experiment_data/P4.json", "package_id": 11},
}


class UserOperationsHandler:

    @staticmethod
    def getUserId(username: str) -> int:
        return USER_MAPPING[username]

    @staticmethod
    def initializeAllUsers(db: Session) -> List[User]:
        for name, id in USER_MAPPING.items():
            db.add(User(id=id, name=name))

    @staticmethod
    def exists(username: str, response: Response) -> bool:
        statusCode = 200 if username.strip() in USER_MAPPING else 404
        response.status_code = statusCode

    @staticmethod
    def getUserPackageMapping() -> Dict[int, Dict]:
        return USER_PACKAGE_MAPPING

    @staticmethod
    def getPackageIdForUser(user_id: int) -> int:
        return USER_PACKAGE_MAPPING[user_id]["package_id"]
