from sentiment import *
from reddit import *
from textblob import TextBlob
import pandas as pd

def get_positive_headlines(keyword):
    positive_headlines = {}
    index = 0
    for headline in get_headlines(keyword):
        sentiment = get_avg_sentiment(headline)
        if sentiment > 0:
            positive_headlines[index] = {}
            positive_headlines[index]["headline"] = headline
            positive_headlines[index]["polarity"] = sentiment
            index += 1
    return positive_headlines

def get_negative_headlines(keyword):
    negative_headlines = {}
    index = 0
    for headline in get_headlines(keyword):
        sentiment = get_avg_sentiment(headline)
        if sentiment < 0:
            negative_headlines[index] = {}
            negative_headlines[index]["headline"] = headline
            negative_headlines[index]["polarity"] = sentiment
            index += 1
    return negative_headlines

def get_word_frequency(headlines):
    words = []
    for index in headlines:
        phrase = headlines[index]['headline']
        blob = TextBlob(phrase)
        for word_tuple in blob.tags:
            if word_tuple[1] == "JJ":
                words.append(word_tuple[0])
            # words.append(word)
    words_series = pd.Series(words)
    return words_series.value_counts(True)

def compare(keyword):
    num_bad = len(get_negative_headlines(keyword))
    num_pos = len(get_positive_headlines(keyword))
    return(str(num_pos - num_bad))

# print(get_word_frequency(get_positive_headlines("btc")))
