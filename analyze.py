from sentiment import *
from reddit import *
from nyt import nyt_article_search
from crypto_panic import get_cryptopanic_latest
from crypto_control import get_crypto_control_top_news
from guardian import guardian_search
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

def analyze_crypto_control():
    entries = get_crypto_control_top_news()
    for index in entries:
        sentiment = get_avg_sentiment(entries[index]["title"])
        entries[index]["polarity"] = sentiment
    return entries

def analyze_guardian(keyword):
    entries = guardian_search(keyword)
    for index in entries:
        sentiment = get_avg_sentiment(entries[index]["title"])
        entries[index]["polarity"] = sentiment
    return entries