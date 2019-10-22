import praw

reddit = praw.Reddit(client_id='_u0PZRm230__1g',
                     client_secret='gXtnAnwhUPz8JFaosTuYKqcYW8w',
                     user_agent='ajl000')


def get_headlines(keyword):
    headlines = set()
    for submission in reddit.subreddit(keyword).new(limit=20):
        headlines.add(submission.title)
    return headlines