from typing import Optional
import logging

import grammar as G

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