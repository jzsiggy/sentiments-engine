from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def get_avg_sentiment(tweet):
    sentiment_sum = 0
    blob = TextBlob(tweet)
    for phrase in blob.sentences:
        sentiment = analyser.polarity_scores(phrase)["compound"]
        sentiment_sum += sentiment
    avg = sentiment_sum / len(blob.sentences)
    return avg

