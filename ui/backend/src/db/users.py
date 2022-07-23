from getpass import getuser
from typing import Dict, List
from random import SystemRandom

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
    # "ibm_P5": 6,
    # "ibm_P1": 7,
    # "ibm_P3": 8,
    # "ibm_P6": 9,
    # "ibm_P2": 10,
    # "ibm_P4": 11,
    # "evaluation_user": 12
}

# user_id => package_info
USER_PACKAGE_MAPPING = {
    1: {"file": "./data/users/data_mansur.json", "package_id": 1},
    2: {"file": "./data/target_set.json", "package_id": 2},
    3: {"file": "./data/users/data_mansur.json", "package_id": 3},
    4: {"file": "./data/users/data_user2.json", "package_id": 4},
    5: {"file": "./data/target_set.json", "package_id": 5},

    # 6: {"file": "./data/experiment_data/P5.json", "package_id": 6},
    # 7: {"file": "./data/experiment_data/P1.json", "package_id": 7},
    # 8: {"file": "./data/experiment_data/P3.json", "package_id": 8},
    # 9: {"file": "./data/experiment_data/P6.json", "package_id": 9},
    # 10: {"file": "./data/experiment_data/P2.json", "package_id": 10},
    # 11: {"file": "./data/experiment_data/P4.json", "package_id": 11},

    # 12: {"file": "./data/evaluation/original12.json", "package_id": 12},
}


class UserOperationsHandler:

    @staticmethod
    def getUserId(username: str, db: Session) -> int:
        user: User = db.query(User) \
            .filter(User.name == username) \
            .first()
        return user.id if user else None

    @staticmethod
    def exists(username: str, response: Response, db: Session):
        userId = UserOperationsHandler.getUserId(username, db)
        response.status_code = 200 if userId else 404

    @staticmethod
    def createNewUser(username: str, db: Session) -> int:
        if UserOperationsHandler.getUserId(username, db) is not None:
            raise Exception("User already exists")
        ids = set(map(lambda user: user.id, db.query(User).all()))
        userId = SystemRandom().randint(150, 1000000)
        while userId in ids:
            userId = SystemRandom().randint(150, 1000000)
        db.add(User(id=userId, name=username))
        return userId
    
    @staticmethod
    def initializeAllPredefinedUsers(db: Session) -> List[User]:
        for name, id in USER_MAPPING.items():
            db.add(User(id=id, name=name))

    @staticmethod
    def getUserPackageMapping() -> Dict[int, Dict]:
        return USER_PACKAGE_MAPPING

    @staticmethod
    def getPackageIdForUser(userId: int) -> int:
        """
        Currently the userId and packageId are the same
        """
        return userId
