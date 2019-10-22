from sentiment import *
from reddit import *
from textblob import TextBlob
import pandas as pd

def get_positive_headlines(keyword):
    positive_headlines = pd.DataFrame(columns=['headline', 'compound'])
    for headline in get_headlines(keyword):
        sentiment = get_avg_sentiment(headline)
        if sentiment > 0:
            positive_headlines = positive_headlines.append({"headline": headline, "compound": sentiment}, ignore_index=True)
    return positive_headlines

def get_negative_headlines(keyword):
    negative_headlines = pd.DataFrame(columns=['headline', 'compound'])
    for headline in get_headlines(keyword):
        sentiment = get_avg_sentiment(headline)
        if sentiment < 0:
            negative_headlines = negative_headlines.append({"headline": headline, "compound": sentiment}, ignore_index=True)
    return negative_headlines

def get_word_frequency(keyword):
    words = []
    headlines = get_negative_headlines(keyword)
    for phrase in headlines.headline:
        # print(phrase)
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

# print(get_word_frequency())
# compare()
