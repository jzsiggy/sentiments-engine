from config import reddit_client_id, reddit_client_secret, reddit_user_agent, nyt_key, guardian_key
import praw
import json
import requests

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

def nyt_article_search(keyword):
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q={0}&api-key={1}".format(keyword, nyt_key)

    response = requests.get(url)
    response = json.loads(response.text)
    results = response["response"]

    payload = {}
    index = 0
    for article in results["docs"]:
        payload[index] = {
            "title" : article["headline"]["print_headline"],
            "url" : article["web_url"],
            "key_words" : [keyword["value"] for keyword in article["keywords"]]
        }

        index+=1
    return payload

def guardian_search(keyword):
    url = 'http://content.guardianapis.com/search?q={0}&api-key={1}'.format(keyword, guardian_key)

    response = requests.get(url)
    response = json.loads(response.text)
    results = response["response"]["results"]

    index = 0
    dic = {}

    for article in results:
        dic[index] = {
            "title": article["webTitle"],
            "url": article["webUrl"],
            "section": article["sectionName"]
        }
        index+=1
    
    return dic