from dataclasses import dataclass
import traceback
from typing import Any, List, Tuple
import json
from sqlalchemy.orm import Session
import format as rulePadFormat
import uuid
from fastapi import Response, UploadFile

from .models import *
from .users import UserOperationsHandler
from .database import JsonRule

@dataclass
class RuleDTO:
    data: Any
    hasPrev: bool
    hasNext: bool
    label: str


class RulePackageNavigation:

    @staticmethod
    def __findNextData(id: int, packageId: int, db: Session) -> Tuple[CandidateRule, bool]:
        results = db.query(CandidateRule) \
            .filter(CandidateRule.package_id == packageId) \
            .order_by(CandidateRule.id.asc()) \
            .all()

        size = len(results)
        for i, data in enumerate(results):
            if data.id == id:
                if i + 1 < size:
                    datum = results[i + 1]
                    hasNext = i + 2 < size
                    return (datum, hasNext)
                else:
                    return (None, False)
        return (None, False)

    @staticmethod
    def __findPrevData(id: int, packageId: int, db: Session) -> Tuple[CandidateRule, bool]:
        results = db.query(CandidateRule) \
            .filter(CandidateRule.package_id == packageId) \
            .order_by(CandidateRule.id.asc()) \
            .all()

        for i, data in enumerate(results):
            if data.id == id:
                if i - 1 >= 0:
                    datum = results[i - 1]
                    hasPrev = i - 2 >= 0
                    return (datum, hasPrev)
                else:
                    return (None, False)
        return (None, False)

    @staticmethod
    def __findNextInDatabase(id: int, userId: int, packageId: int, db: Session) -> RuleDTO:
        datum, hasNext = RulePackageNavigation.__findNextData(id, packageId, db)
        if datum:
            return RulePackageNavigation.__candidateRuleToDTO(db, datum, userId, hasPrev=True, hasNext=hasNext)
        return RuleDTO(None, False, False, False)

    @staticmethod
    def __findPrevInDatabase(id: int, userId: int, packageId: int, db: Session) -> RuleDTO:
        datum, hasPrev = RulePackageNavigation.__findPrevData(id, packageId, db)
        if datum:
            return RulePackageNavigation.__candidateRuleToDTO(db, datum, userId, hasPrev=hasPrev, hasNext=True)
        return RuleDTO(None, False, False, False)

    @staticmethod
    def __getLabelAndRuleString(db: Session, ruleObj: CandidateRule, userId: int):
        name = db.query(CandidateRulesPackage).filter(
            CandidateRulesPackage.id == ruleObj.package_id).first().name
        size = db.query(CandidateRule).filter(
            CandidateRule.package_id == ruleObj.package_id).count()

        totalLabeledRuleCount = RuleLabelingHandler.getLabeledRuleCount(db, userId)

        labeledRule = db.query(LabeledRule).filter_by(
            candidate_rule_id=ruleObj.id, user_id=userId).first()

        if labeledRule and labeledRule.label == RuleLabels.CORRECT:
            return (labeledRule.label, labeledRule.rule_description, name, size, totalLabeledRuleCount)

        label = labeledRule.label if labeledRule else RuleLabels.UNLABELED
        # re-generate the rule description if:
        # - the rule has not been labeled
        # - the rule has been labeled as 'not_a_rule'
        antecedents: List[str] = json.loads(ruleObj.antecedent)
        consequents: List[str] = json.loads(ruleObj.consequent)

        ruleString = rulePadFormat.toShortRulePad(rulePadFormat.JsonRule(
            id=id,
            antecedent=antecedents,
            consequent=consequents)
        )

        return (label, ruleString, name, size, totalLabeledRuleCount)

    @staticmethod
    def __candidateRuleToDTO(db: Session, ruleObj: CandidateRule, userId: int, hasPrev: bool, hasNext: bool) -> RuleDTO:
        """
            it takes a candidate rule object with some extra data (hasPrev, hasNext) 
            and constructs a RuleDTO object with the correct label
        """
        label, ruleString, name, size, totalLabeledRuleCount = \
                                RulePackageNavigation.__getLabelAndRuleString(db, ruleObj, userId)
        return RuleDTO(data={
            "id": ruleObj.id,
            "ruleString": ruleString,
            "name": name,
            "size": size,
            "totalLabeledRuleCount": totalLabeledRuleCount
        }, hasPrev=hasPrev, hasNext=hasNext, label=label)

    @staticmethod
    def getNext(db: Session, id: int, userId: int) -> RuleDTO:
        """
            gets the candidate rule and its label after the given 'id'
            if 'id' is not given, then it will return the first element of the rule package
        """
        packageId = UserOperationsHandler.getPackageIdForUser(userId)
        if id is None:
            firstElement = db.query(CandidateRule) \
                .filter(CandidateRule.package_id == packageId) \
                .order_by(CandidateRule.id.asc()) \
                .first()
            # FIXME: hasNext can be false
            return RulePackageNavigation.__candidateRuleToDTO(db, firstElement, userId, False, True)
        return RulePackageNavigation.__findNextInDatabase(id, userId, packageId, db)

    @staticmethod
    def getPrev(db: Session, id: int, userId: int) -> RuleDTO:
        """
            gets the candidate rule and its label before the given 'id'
            if 'id' is not given, then it will return the first element of the rule package
        """
        packageId = UserOperationsHandler.getPackageIdForUser(userId)
        if id is None:
            firstElement = db.query(CandidateRule) \
                .filter(CandidateRule.package_id == packageId) \
                .order_by(CandidateRule.id.asc()) \
                .first()
            # FIXME: hasNext can be false
            return RulePackageNavigation.__candidateRuleToDTO(db, firstElement, userId, False, True)
        return RulePackageNavigation.__findPrevInDatabase(id, userId, packageId, db)


class RuleLabelingHandler:

    def labelRule(db: Session, id: int, rulePadString: str, label: str, userId: int):
        """
            Labels the rule with the given id as 'correct', 'best_practice' or 'not_a_rule'. 
            It also saves the rulePadString (which can be empty)
        """
        RuleLabels.assertThatLabelIsSupported(label)

        labelFromDatabase = db.query(LabeledRule).filter_by(
            candidate_rule_id=id, user_id=userId).first()

        if labelFromDatabase is None:
            db.add(LabeledRule(
                id=str(uuid.uuid4()),
                candidate_rule_id=id,
                rule_description=rulePadString,
                label=label,
                user_id=userId
            ))
        else:
            labelFromDatabase.label = label
            labelFromDatabase.rule_description = rulePadString
        db.commit()

    def unlabelRule(db: Session, id: int, userId: int):
        """
            Removes the label from a rule with the given id
        """
        labelFromDatabase = db.query(LabeledRule).filter_by(
            candidate_rule_id=id, user_id=userId).first()
        if labelFromDatabase:
            db.delete(labelFromDatabase)
            db.commit()

    def getLabeledRuleCount(db: Session, userId: int) -> int:
        # TODO: this should be achieved by joining 2 tables and 
        # getting the results by using package_id, however, at the current setting
        # package_id and user_id have 1 to 1 mapping 
        return db.query(LabeledRule).filter_by(
            user_id=userId).count()


class RulePackageOperations:

    def createNewPackage(username: str, packageName: str, rulesFile: UploadFile, resp: Response, db: Session):
        try:
            if rulesFile.content_type != "application/json":
                raise Exception("Unsupported file type: [%s]" % (rulesFile.content_type))
            # parse all provided rules into RulePad rules
            jsonFileContents = json.loads(rulesFile.file.read())
            rules = map(lambda x: JsonRule(x["id"], x["antecedent"], x["consequent"]), jsonFileContents)
            # create a user with id X
            userId = UserOperationsHandler.createNewUser(username, db)
            # create a package with id X
            if packageName is None or packageName.strip() == "":
                packageName = "MicroProfile Candidate Rules"

            db.add(CandidateRulesPackage(id = userId, name = packageName))
            # add all the rules for that user
            for rule in rules:
                db.add(CandidateRule(
                    counter=str(uuid.uuid4()), 
                    id=rule.id, 
                    antecedent=rule.get_antecedent(),
                    consequent=rule.get_consequent(), 
                    package_id = userId
                ))
            db.commit()
        except Exception as e:
            if e.args[0] == "User already exists":
                resp.status_code = 409 # Http Conflict
            else:
                resp.status_code = 422
                traceback.print_exc()
                print(e)


    def getAllConfirmedRules(db: Session):
        return RulePackageOperations.__getConfirmedRulesByFilter(db,
            LabeledRule.label.in_([RuleLabels.CORRECT, RuleLabels.BEST_PRACTICE])
        )

    def getConfirmedRulesByPackageId(packageId: int, db: Session):
        return RulePackageOperations.__getConfirmedRulesByFilter(db,
            LabeledRule.user_id == packageId,
            LabeledRule.label.in_([RuleLabels.CORRECT, RuleLabels.BEST_PRACTICE])
        )

    def __getConfirmedRulesByFilter(db: Session, *filters):
        # get confirmed rules
        confirmedLabeledRules: List[LabeledRule] = db.query(LabeledRule)\
            .filter(*filters)\
            .all()
        
        def labeledRuleToObj(r: LabeledRule):
            return {
                "id": r.id, 
                "specification": r.rule_description,
                "is_best_practice": r.label == RuleLabels.BEST_PRACTICE
            }

        return {
            "rules": list(map(labeledRuleToObj, confirmedLabeledRules))
        }

class RuleLabels:
    CORRECT = "correct"
    BEST_PRACTICE = "best_practice"
    INCORRECT = "not_a_rule"
    UNLABELED = "unlabeled"

    def checkIfLabelIsSupported(label: str) -> bool:
        return label in {RuleLabels.CORRECT, RuleLabels.BEST_PRACTICE, RuleLabels.INCORRECT}

    def assertThatLabelIsSupported(label: str) -> bool:
        assert RuleLabels.checkIfLabelIsSupported(label), \
            f"Label '{label}' is not supported, it needs to be one of ['correct', 'best_practice', 'not_a_rule']"
    
    def getAll() -> List[str]:
        return [RuleLabels.CORRECT, RuleLabels.BEST_PRACTICE, RuleLabels.INCORRECT, RuleLabels.UNLABELED]