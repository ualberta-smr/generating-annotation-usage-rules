from dataclasses import dataclass
from typing import Any, List, Tuple
from enum import Enum
import json
from sqlalchemy.orm import Session
import rulepadFormat as rf
import uuid

from .models import *
from .constants import DEFAULT_USER_ID


@dataclass
class RuleDTO:
    data: Any
    hasPrev: bool
    hasNext: bool
    label: str


class RuleLabels(Enum):
    CORRECT = 1
    NOT_A_RULE = 2


class RulePackageNavigation:

    @staticmethod
    def __findNextData(id: int, db: Session) -> Tuple[CandidateRule, bool]:
        results = db.query(CandidateRule).all()
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
    def __findPrevData(id: int, db: Session) -> Tuple[CandidateRule, bool]:
        results = db.query(CandidateRule).all()
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
    def __findNextInDatabase(id: int, db: Session) -> RuleDTO:
        datum, hasNext = RulePackageNavigation.__findNextData(id, db)
        if datum:
            return RulePackageNavigation.__candidateRuleToDTO(db, datum, hasPrev=True, hasNext=hasNext)
        return RuleDTO(None, False, False, False)

    @staticmethod
    def __findPrevInDatabase(id: int, db: Session) -> RuleDTO:
        datum, hasPrev = RulePackageNavigation.__findPrevData(id, db)
        if datum:
            return RulePackageNavigation.__candidateRuleToDTO(db, datum, hasPrev=hasPrev, hasNext=True)
        return RuleDTO(None, False, False, False)

    @staticmethod
    def __candidateRuleToDTO(db: Session, ruleObj: CandidateRule, hasPrev: bool, hasNext: bool) -> RuleDTO:
        """
            it takes a candidate rule object with some extra data (hasPrev, hasNext) 
            and constructs a RuleDTO object with the correct label
        """
        antecedents: List[str] = json.loads(ruleObj.antecedent)
        consequents: List[str] = json.loads(ruleObj.consequent)
        ruleString = rf.toShortRulePad(rf.JsonRule(
            id=id,
            antecedent=antecedents,
            consequent=consequents)
        )

        labeledRule = db.query(LabeledRule).filter_by(
            candidate_rule_id=ruleObj.id).first()
        label = "unlabeled"
        if labeledRule:
            label = labeledRule.label

        return RuleDTO(data={
            "id": ruleObj.id,
            "ruleString": ruleString
        }, hasPrev=hasPrev, hasNext=hasNext, label=label)

    @staticmethod
    def getNext(db: Session, id: int) -> RuleDTO:
        """
            gets the candidate rule and its label after the given 'id'
            if 'id' is not given, then it will return the first element of the rule package
        """
        if id is None:
            firstElement = db.query(CandidateRule).first()
            # FIXME: hasNext can be false
            return RulePackageNavigation.__candidateRuleToDTO(db, firstElement, False, True)
        return RulePackageNavigation.__findNextInDatabase(id, db)

    @staticmethod
    def getPrev(db: Session, id: int) -> RuleDTO:
        """
            gets the candidate rule and its label before the given 'id'
            if 'id' is not given, then it will return the first element of the rule package
        """
        if id is None:
            firstElement = db.query(CandidateRule).first()
            # FIXME: hasNext can be false
            return RulePackageNavigation.__candidateRuleToDTO(db, firstElement, False, True)
        return RulePackageNavigation.__findPrevInDatabase(id, db)


class RuleLabelingHandler:

    def labelRule(db: Session, id: int, rulePadString: str, label: str):
        """
            Labels the rule with the given id as 'correct' or 'not_a_rule'. 
            It also saves the rulePadString (which can be empty)
        """
        assert label in ["correct", "not_a_rule"], \
            f"Label '{label}' is not supported, it needs to be one of ['correct', 'not_a_rule']"

        # update the rule
        labelFromDatabase = db.query(LabeledRule).filter_by(
            candidate_rule_id=id).first()
        if labelFromDatabase is None:
            db.add(LabeledRule(
                id=str(uuid.uuid4()),
                candidate_rule_id=id,
                rule_description=rulePadString,
                label=label,
                user_id=DEFAULT_USER_ID
            ))
        else:
            labelFromDatabase.label = label
            labelFromDatabase.rule_description = rulePadString
        db.commit()

    def unlabelRule(db: Session, id: int):
        """
            Removes the label from a rule with the given id
        """
        labelFromDatabase = db.query(LabeledRule).filter_by(
            candidate_rule_id=id).first()
        db.delete(labelFromDatabase)
        db.commit()
