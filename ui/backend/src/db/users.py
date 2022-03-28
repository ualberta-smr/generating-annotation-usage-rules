from typing import List

from fastapi import Response
from .models import User
from sqlalchemy.orm import Session


USER_MAPPING = {
    "mansur": 1,
    "emily": 2,
    "user1": 3,
    "user2": 4,
    "user3": 5,
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
        if username.strip() in USER_MAPPING:
            response.status_code = 200
        else:
            response.status_code = 404
        