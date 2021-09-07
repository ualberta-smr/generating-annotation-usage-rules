from typing import Optional
import logging
import traceback

import grammar as G
import database as DB

from fastapi import FastAPI, Response
from fastapi.logger import logger as fastapi_logger
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers

fastapi_logger.handlers = gunicorn_error_logger.handlers
fastapi_logger.setLevel(logging.INFO)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init db
db = DB.Database()
db.initialize()


def get_config(config):
    if config:
        return {
            "filename": config[0],
            "code": config[1]
        }
    return None


@app.get('/grammarToCode')
def index(response: Response, grammar: Optional[str] = ""):
    try:
        grammar = grammar.strip() + " "
        print(f"Requested: [{grammar}]")
        code, config = G.convert(grammar)
        response.status_code = 200
        return {
            "code": code,
            "configuration": get_config(config)
        }
    except Exception as e:
        traceback.print_exc()
        print(e)
        response.status_code = 400
        return {
            "code": None,
            "configuration": None
        }

def __getRule(rule_id: int, response: Response, next=True):
    try:
        r = db.getNext(rule_id) if next else db.getPrev(rule_id)
        if r and r.data:
            rule_string = r.data["ruleString"]
            code, config = G.convert(rule_string)
            r.data["grammar"] = {
                "code": code,
                "configuration": get_config(config)
            }
        response.status_code = 200
        return r
    except Exception as e:
        traceback.print_exc()
        print(e)
        print(r)
        response.status_code = 400
        return DB.RuleDTO(None, False, False, False)

@app.get('/rules')
def getFirstRule(response: Response):
    return __getRule(None, response)

@app.get('/rules/{rule_id}/next')
def getNextRule(rule_id: int, response: Response):
    return __getRule(rule_id, response)

@app.get('/rules/{rule_id}/prev')
def getPrevRule(rule_id: int, response: Response):
    return __getRule(rule_id, response, next=False)

class ConfirmRuleDTO(BaseModel):
    ruleString: str

@app.post('/rules/{rule_id}/{label}')
def labelRule(rule_id: int, label: str, response: Response, ruleDto: Optional[ConfirmRuleDTO] = None):
    try:
        if label == "correct":
            db.labelRuleCorrect(rule_id, ruleDto.ruleString)
        elif label == "not_a_rule":
            db.labelNotARule(rule_id)
        elif label == "unlabeled":
            db.unlabel(rule_id)
        response.status_code = 204
    except Exception as e:
        traceback.print_exc()
        print(e)
        response.status_code = 400