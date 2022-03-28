from typing import Optional, List
import logging
import traceback

from sqlalchemy.orm.session import Session
from api import RuleOperationsHandler, ConfirmRuleDTO

import grammar as G

from db import SessionLocal, models, schemas, createAndInitializeDb, RulePackageOperations, UserOperationsHandler

from fastapi import FastAPI, Response, Depends
from fastapi.logger import logger as fastapi_logger
from fastapi.middleware.cors import CORSMiddleware

gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers

fastapi_logger.handlers = gunicorn_error_logger.handlers
fastapi_logger.setLevel(logging.INFO)

createAndInitializeDb()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_config(config):
    if config:
        return {
            "filename": config[0],
            "code": config[1]
        }
    return None


@app.get("/getAll", response_model=List[schemas.CandidateRule])
def getAll(db: Session = Depends(get_db)):
    return db.query(models.CandidateRule).all()


@app.get('/grammarToCode')
def grammarToCode(response: Response, grammar: Optional[str] = ""):
    EMPTY_RESPONSE = {
        "code": None,
        "configuration": None
    }
    
    try:
        if grammar.strip() == "":
            response.status_code = 200
            return EMPTY_RESPONSE

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
        return EMPTY_RESPONSE


@app.get('/rules')
def getFirstRule(user_id: str, response: Response, db: Session = Depends(get_db)):
    return RuleOperationsHandler.getFirstRule(user_id, response, db)


@app.get('/rules/{rule_id}/next')
def getNextRule(rule_id: int, user_id: str, response: Response, db: Session = Depends(get_db)):
    return RuleOperationsHandler.getNextRule(rule_id, user_id, response, db)


@app.get('/rules/{rule_id}/prev')
def getPrevRule(rule_id: int, user_id: str, response: Response, db: Session = Depends(get_db)):
    return RuleOperationsHandler.getPrevRule(rule_id, user_id, response, db)


@app.post('/rules/{rule_id}/{label}')
def labelRule(rule_id: int, label: str, response: Response, ruleDto: Optional[ConfirmRuleDTO] = None, db: Session = Depends(get_db)):
    RuleOperationsHandler.labelRule(rule_id, label, response, ruleDto, db)

@app.get('/packages/{package_id}/confirmed')
def getRulesPackage(package_id: int, db: Session = Depends(get_db)):
    return RulePackageOperations.getConfirmedRulesByPackageId(package_id, db)

@app.get('/users')
def checkIfUserExists(q: str, response: Response):
    UserOperationsHandler.exists(q, response)