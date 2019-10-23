import json
import requests
from config import nyt_key

def nyt_article_search(keyword):
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q={0}&api-key={1}".format(keyword, nyt_key)

    response = requests.get(url)
    response = json.loads(response.text)
    results = response["response"]

    for article in results["docs"]:
        print(article["headline"]["print_headline"])

nyt_article_search("bitcoin")