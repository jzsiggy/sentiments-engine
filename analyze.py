from sentiment import *
from reddit import *
from nyt import nyt_article_search
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