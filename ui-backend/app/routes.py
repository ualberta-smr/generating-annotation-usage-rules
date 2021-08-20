from app import app
from flask import request
import grammar as G
import logging

logging.basicConfig(level=logging.INFO)

@app.route('/grammarToCode')
def index():
    try:
        grammar = request.args["grammar"]
        grammar = grammar.strip() + " "
        app.logger.info(f"Requested: [{grammar}]")
        code, properties = G.convert(grammar)
        return {
            "code": code, 
            "properties": properties
        }, 200
    except Exception as e:
        app.logger.error(e)
        return {
            "code": "",
            "properties": None
        }, 401