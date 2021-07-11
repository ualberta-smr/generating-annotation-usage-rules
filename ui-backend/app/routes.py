from app import app
from flask import request
from grammar.converter import *

@app.route('/grammarToCode')
def index():
    try:
        grammar = request.args["grammar"]
        code = convert(grammar)
        return {
            "code": code
        }, 200
    except Exception as e:
        print(e)
        return {
            "code": ""
        }, 401