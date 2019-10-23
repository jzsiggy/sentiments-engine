import json
import requests

def nyt_article_search(keyword):
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q={}&api-key=pJ0gt0GDWxElOgFrhJ43gQq6sc2JLT8p".format(keyword)

    response = requests.get(url)
    response = json.loads(response.text)
    results = response["response"]

    for article in results["docs"]:
        print(article["headline"]["print_headline"])

nyt_article_search("bitcoin")