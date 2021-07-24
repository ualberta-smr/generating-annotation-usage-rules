from app import app
from flask import request
import grammar as G

@app.route('/grammarToCode')
def index():
    try:
        grammar = request.args["grammar"]
        code, properties = G.convert(grammar)
        return {
            "code": code, 
            "properties": properties
        }, 200
    except Exception as e:
        print(e)
        return {
            "code": "",
            "properties": None
        }, 401