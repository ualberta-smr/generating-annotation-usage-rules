from logging import Logger
from db import RuleDTO, RuleLabelingHandler, RulePackageNavigation, RuleLabels, UserOperationsHandler
from sqlalchemy.orm.session import Session
from fastapi import Response
import traceback
from pydantic import BaseModel
from typing import Optional

class ConfirmRuleDTO(BaseModel):
    ruleString: str
    username: str


class RuleOperationsHandler:

    EMPTY_RULE_DTO = RuleDTO(None, False, False, False)

    @staticmethod
    def __getRule(db: Session, ruleId: int, userId: str, response: Response, next=True):
        try:
            userId = UserOperationsHandler.getUserId(userId)
            r = RulePackageNavigation.getNext(db, ruleId, userId) if next \
                else RulePackageNavigation.getPrev(db, ruleId, userId)
            if r and r.data:
                response.status_code = 200
                return r
            response.status_code = 404
            return RuleOperationsHandler.EMPTY_RULE_DTO
        except Exception as e:
            traceback.print_exc()
            print(e)
            response.status_code = 400
            return RuleOperationsHandler.EMPTY_RULE_DTO

    @staticmethod
    def getFirstRule(userId: str, response: Response, db: Session):
        return RuleOperationsHandler.__getRule(db, None, userId, response)

    @staticmethod
    def getNextRule(ruleId: int, userId: str, response: Response, db: Session):
        return RuleOperationsHandler.__getRule(db, ruleId, userId, response)

    @staticmethod
    def getPrevRule(ruleId: int, userId: str, response: Response, db: Session):
        return RuleOperationsHandler.__getRule(db, ruleId, userId, response, next=False)

    @staticmethod
    def labelRule(ruleId: int, label: str, response: Response, ruleDto: Optional[ConfirmRuleDTO], db: Session):
        try:
            userId = UserOperationsHandler.getUserId(ruleDto.username)
            if userId is None:
                raise Exception(f"Username {ruleDto.username} does not exist")
                
            if RuleLabels.checkIfLabelIsSupported(label):
                rulePadString = ruleDto.ruleString if label in [RuleLabels.CORRECT, RuleLabels.BEST_PRACTICE] else ""
                RuleLabelingHandler.labelRule(
                    db=db,
                    id=ruleId,
                    rulePadString=rulePadString,
                    label=label,
                    userId=userId
                )
            elif label == RuleLabels.UNLABELED:
                RuleLabelingHandler.unlabelRule(
                    db=db, id=ruleId, userId=userId)
            else:
                raise Exception(
                    f"Rule label string needs to be one of [{RuleLabels.getAll()}]")
            response.status_code = 200
            return {
                "totalLabeledRuleCount": RuleLabelingHandler.getLabeledRuleCount(db, userId)
            }
        except Exception as e:
            traceback.print_exc()
            print(e)
            response.status_code = 400
