from analyze import analyze_reddit_headlines, analyze_newYorkTimes_headlines, analyze_crypto_panic, analyze_crypto_control, analyze_guardian
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

@app.route('/crypto-panic')
def crypto_panic():
    keyword = request.args['keyword']
    return jsonify(analyze_crypto_panic(keyword))

@app.route('/crypto-control')
def crypto_control():
    return jsonify(analyze_crypto_control())

@app.route('/guardian')
def guardian():
    keyword = request.args['keyword']
    return jsonify(analyze_guardian(keyword))