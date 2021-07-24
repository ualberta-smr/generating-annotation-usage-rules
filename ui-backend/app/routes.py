from app import app
from flask import request
import grammar as G

@app.route('/grammarToCode')
def index():
    try:
        grammar = request.args["grammar"]
        code = G.convert(grammar)
        return {
            "code": code
        }, 200
    except Exception as e:
        print(e)
        return {
            "code": ""
        }, 401