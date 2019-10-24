from config import reddit_client_id, reddit_client_secret, reddit_user_agent
import praw

reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)


def get_reddit_headlines(keyword):
    headlines = {}
    index = 0
    for submission in reddit.subreddit(keyword).hot(limit=10):
        headlines["{}".format(index)] = {
            "title" : submission.title,
            # "comments" : [comment.body for comment in submission.comments],
            "url" : submission.url
        }
        index+=1

    return headlines
