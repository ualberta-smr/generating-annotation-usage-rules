from os import getenv
import json
from typing import List, Iterator
from dataclasses import dataclass
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from .models import User, Base, CandidateRule, CandidateRulesPackage
from .users import UserOperationsHandler

SQL_ALCHEMY_DATABASE_URL = getenv("DB_URL")

engine = create_engine(SQL_ALCHEMY_DATABASE_URL, pool_recycle=300)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@dataclass
class JsonRule:
    id: int
    antecedent: List[str]
    consequent: List[str]

    def get_antecedent(self) -> str:
        return json.dumps(self.antecedent)
    
    def get_consequent(self) -> str:
        return json.dumps(self.consequent)

def __getDataFromSourceMicroProfile(filename: str) -> Iterator[JsonRule]:
    with open(filename) as j:
        values = json.load(j)
        return map(lambda x: JsonRule(x["id"], x["antecedent"], x["consequent"]), values)

def __populate(db: Session):
    # create a user
    UserOperationsHandler.initializeAllPredefinedUsers(db)

    for user_id, package_data in UserOperationsHandler.getUserPackageMapping().items():
        db.add(CandidateRulesPackage(id = package_data["package_id"], name = "MicroProfile Candidate Rules"))

        for rule in __getDataFromSourceMicroProfile(package_data["file"]):
            db.add(CandidateRule(
                counter=str(uuid.uuid4()), 
                id=rule.id, 
                antecedent=rule.get_antecedent(), 
                consequent=rule.get_consequent(), 
                package_id = package_data["package_id"]
            ))

    db.commit()

def createAndInitializeDb():
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        if db.query(User).count() == 0:
            __populate(db)