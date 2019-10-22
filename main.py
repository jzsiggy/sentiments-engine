from analyze import compare, get_negative_headlines, get_positive_headlines
from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Home"

@app.route('/positive')
def positive():
    keyword = request.args['keyword']
    return get_positive_headlines(keyword).to_json()

@app.route('/negative')
def negative():
    keyword = request.args['keyword']
    return get_negative_headlines(keyword).to_json()