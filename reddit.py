from config import client_id, client_secret, user_agent
import praw

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)


def get_headlines(keyword):
    headlines = set()
    for submission in reddit.subreddit(keyword).hot(limit=200):
        headlines.add(submission.title)
    return headlines

def test():
    for submission in reddit.subreddit("bitcoin").hot(limit=1):
        for comment in submission.comments:
            print(comment.body)
# test()