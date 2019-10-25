from sentiment import *

from news import nyt_article_search, guardian_search, get_reddit_headlines

from crypto import get_crypto_control_top_news, get_cryptopanic_latest

from textblob import TextBlob
import pandas as pd

def analyze_reddit_headlines(keyword):
    submissions = get_reddit_headlines(keyword)
    for index in submissions:
        sentiment = get_avg_sentiment(submissions[index]["title"])
        submissions[index]["polarity"] = sentiment
    return submissions


def analyze_newYorkTimes_headlines(keyword):
    articles = nyt_article_search(keyword)
    for index in articles:
        if (articles[index]["title"]):
            sentiment = get_avg_sentiment(articles[index]["title"])
            articles[index]["polarity"] = sentiment
    return articles

def analyze_crypto_panic(keyword):
    submissions = get_cryptopanic_latest(keyword)
    for index in submissions:
        sentiment = get_avg_sentiment(submissions[index]["title"])
        submissions[index]["polarity"] = sentiment
    return submissions

def analyze_guardian(keyword):
    entries = guardian_search(keyword)
    for index in entries:
        sentiment = get_avg_sentiment(entries[index]["title"])
        entries[index]["polarity"] = sentiment
    return entries

def analyze_crypto_control():
    entries = get_crypto_control_top_news()
    for index in entries:
        sentiment = get_avg_sentiment(entries[index]["title"])
        entries[index]["polarity"] = sentiment
    return entries