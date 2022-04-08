from db import RuleDTO, RuleLabelingHandler, RulePackageNavigation, RuleLabels, UserOperationsHandler
from sqlalchemy.orm.session import Session
from fastapi import Response
import traceback
from pydantic import BaseModel
from typing import Optional
import grammar as G


class ConfirmRuleDTO(BaseModel):
    ruleString: str
    username:str


def get_config(config):
    if config:
        return {
            "filename": config[0],
            "code": config[1]
        }
    return None


class RuleOperationsHandler:

    @staticmethod
    def __getRule(db: Session, rule_id: int, user_id: int, response: Response, next=True):
        try:
            r = RulePackageNavigation.getNext(
                db, rule_id, user_id) if next else RulePackageNavigation.getPrev(db, rule_id, user_id)
            if r and r.data:
                rule_string = r.data["ruleString"]
                code, config = G.convert(rule_string)
                r.data["grammar"] = {
                    "code": code,
                    "configuration": config
                }
                response.status_code = 200
                return r
            response.status_code = 404
            return RuleDTO(None, False, False, False)
        except Exception as e:
            traceback.print_exc()
            print(e)
            response.status_code = 400
            return RuleDTO(None, False, False, False)

    @staticmethod
    def getFirstRule(user_id: str, response: Response, db: Session):
        user_id = UserOperationsHandler.getUserId(user_id)
        return RuleOperationsHandler.__getRule(db, None, user_id, response)

    @staticmethod
    def getNextRule(rule_id: int, user_id: str, response: Response, db: Session):
        user_id = UserOperationsHandler.getUserId(user_id)
        return RuleOperationsHandler.__getRule(db, rule_id, user_id, response)

    @staticmethod
    def getPrevRule(rule_id: int, user_id: str, response: Response, db: Session):
        user_id = UserOperationsHandler.getUserId(user_id)
        return RuleOperationsHandler.__getRule(db, rule_id, user_id, response, next=False)

    @staticmethod
    def labelRule(rule_id: int, label: str, response: Response, ruleDto: Optional[ConfirmRuleDTO], db: Session):
        try:
            user_id = UserOperationsHandler.getUserId(ruleDto.username)
            if RuleLabels.label_is_supported(label):
                rulePadString = ruleDto.ruleString if label == RuleLabels.CORRECT else ""
                RuleLabelingHandler.labelRule(
                    db=db,
                    id=rule_id,
                    rulePadString=rulePadString,
                    label=label,
                    user_id=user_id
                )
            elif label == RuleLabels.UNLABELED:
                RuleLabelingHandler.unlabelRule(db=db, id=rule_id, user_id=user_id)
            else:
                raise Exception(
                    f"Rule label string needs to be one of [{RuleLabels.get_all()}]")
            response.status_code = 204
        except Exception as e:
            traceback.print_exc()
            print(e)
            response.status_code = 400
