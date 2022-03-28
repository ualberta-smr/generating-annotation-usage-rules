import uuid
from .database import *
from .operations import RuleDTO, RuleLabelingHandler, RulePackageNavigation, RulePackageOperations
from .models import User, Base, CandidateRule, CandidateRulesPackage
from .constants import *
from .users import UserOperationsHandler

import json
from typing import List, Iterator
from dataclasses import dataclass
from sqlalchemy.orm.session import Session

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
    UserOperationsHandler.initializeAllUsers(db)
    # db.add(CandidateRulesPackage(id = DEFAULT_PACKAGE_ID, name = "MicroProfile Candidate Rules"))
    # db.commit()
    # # create a package
    # for rule in __getDataFromSourceMicroProfile():
    #     db.add(CandidateRule(id=rule.id, antecedent=rule.get_antecedent(), consequent=rule.get_consequent(), package_id = DEFAULT_PACKAGE_ID))

    # db.commit()

    for user_id, package_data in UserOperationsHandler.getUserPackageMapping().items():
        db.add(CandidateRulesPackage(id = package_data["package_id"], name = "MicroProfile Candidate Rules"))

        for rule in __getDataFromSourceMicroProfile(package_data["file"]):
            db.add(CandidateRule(counter=str(uuid.uuid4()), id=rule.id, antecedent=rule.get_antecedent(), consequent=rule.get_consequent(), package_id = package_data["package_id"]))

    db.commit()

def createAndInitializeDb():
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        if db.query(User).count() == 0:
            __populate(db)