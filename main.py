from analyze import analyze_reddit_headlines, analyze_newYorkTimes_headlines
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "Home"

@app.route('/reddit')
def reddit():
    keyword = request.args['keyword']
    return jsonify(analyze_reddit_headlines(keyword))

@app.route('/nyt')
def nyt():
    keyword = request.args['keyword']
    return jsonify(analyze_newYorkTimes_headlines(keyword))