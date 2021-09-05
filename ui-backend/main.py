from typing import Optional
import logging

import grammar as G
import database as DB

from fastapi import FastAPI, Response
from fastapi.logger import logger as fastapi_logger
from fastapi.middleware.cors import CORSMiddleware

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
        import traceback
        traceback.print_exc()
        print(e)
        response.status_code = 401
        return {
            "code": None,
            "configuration": None
        }

def __getRule(rule_id: int, response: Response):
    try:
        r = db.getNext(rule_id)
        if r and r["data"]:
            rule_string = r["data"]["rule_string"]
            code, config = G.convert(rule_string)
            r["data"]["grammar"] = {
                "code": code,
                "configuration": get_config(config)
            }
        return r

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(e)
        response.status_code = 401
        return {
            "data": None,
            "hasNext": False
        }

@app.get('/rules')
def getRule(response: Response):
    return __getRule(None, response)

@app.get('/rules/{rule_id}')
def getRule(rule_id: int, response: Response):
    return __getRule(rule_id, response)
