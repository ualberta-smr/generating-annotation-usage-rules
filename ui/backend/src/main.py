from typing import Optional
import logging

from sqlalchemy.orm.session import Session
from fastapi import FastAPI, Response, Depends
from fastapi.logger import logger
from fastapi.middleware.cors import CORSMiddleware

from api import RuleOperationsHandler, ConfirmRuleDTO, GrammarOperationsHandler
from db import SessionLocal, createAndInitializeDb, RulePackageOperations, UserOperationsHandler

gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers

logger.handlers = gunicorn_error_logger.handlers
logger.setLevel(logging.INFO)

createAndInitializeDb()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def getSession():
    try:
        sl = SessionLocal()
        yield sl
    finally:
        sl.close()


@app.get('/grammarToCode')
def grammarToCode(response: Response, grammar: Optional[str] = ""):
    return GrammarOperationsHandler.generateJavaPreviewCode(grammar, response, logger)


@app.get('/rules')
def getFirstRule(userId: str, response: Response, db: Session = Depends(getSession)):
    return RuleOperationsHandler.getFirstRule(userId, response, db)


@app.get('/rules/{ruleId}/next')
def getNextRule(ruleId: int, userId: str, response: Response, db: Session = Depends(getSession)):
    return RuleOperationsHandler.getNextRule(ruleId, userId, response, db)


@app.get('/rules/{ruleId}/prev')
def getPrevRule(ruleId: int, userId: str, response: Response, db: Session = Depends(getSession)):
    return RuleOperationsHandler.getPrevRule(ruleId, userId, response, db)


@app.post('/rules/{ruleId}/{label}')
def labelRule(ruleId: int, label: str, response: Response, ruleDto: Optional[ConfirmRuleDTO] = None, db: Session = Depends(getSession)):
    return RuleOperationsHandler.labelRule(ruleId, label, response, ruleDto, db)

@app.get('/packages/{packageId}/confirmed')
def getRulesPackage(packageId: int, db: Session = Depends(getSession)):
    return RulePackageOperations.getConfirmedRulesByPackageId(packageId, db)

@app.get('/users')
def checkIfUserExists(q: str, response: Response):
    UserOperationsHandler.exists(q, response)