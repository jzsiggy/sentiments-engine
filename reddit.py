from config import client_id, client_secret, user_agent
import praw

reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)


def get_reddit_headlines(keyword):
    headlines = set()
    for submission in reddit.subreddit(keyword).hot(limit=200):
        headlines.add(submission.title)
    return headlines