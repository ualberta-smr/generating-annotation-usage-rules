import traceback
from typing import Dict, List

from fastapi import Response
from .models import User
from sqlalchemy.orm import Session


# username => user_id
USER_MAPPING = {
    # dummy data
    "mansur": 1,
    "ajay": 2,
    "demo": 3,
    "user2": 4,
    "user3": 5,
    # experiment subjects
    "ibm_P5": 6,
    "ibm_P1": 7,
    "ibm_P3": 8,
    "ibm_P6": 9,
    "ibm_P2": 10,
    "ibm_P4": 11
}

# user_id => package_info
USER_PACKAGE_MAPPING = {
    1: {"file": "./data/users/data_mansur.json", "package_id": 1},
    2: {"file": "./data/target_set.json", "package_id": 2},
    3: {"file": "./data/users/data_mansur.json", "package_id": 3},
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
        if username not in USER_MAPPING:
            return None
        return USER_MAPPING[username]

    @staticmethod
    def initializeAllUsers(db: Session) -> List[User]:
        for name, id in USER_MAPPING.items():
            db.add(User(id=id, name=name))

    @staticmethod
    def exists(username: str, response: Response) -> bool:
        try:
            statusCode = 200 if username.strip() in USER_MAPPING else 404
            response.status_code = statusCode
        except Exception as e:
            traceback.print_exc()
            print(e)
            response.status_code = 404

    @staticmethod
    def getUserPackageMapping() -> Dict[int, Dict]:
        return USER_PACKAGE_MAPPING

    @staticmethod
    def getPackageIdForUser(user_id: int) -> int:
        return USER_PACKAGE_MAPPING[user_id]["package_id"]
