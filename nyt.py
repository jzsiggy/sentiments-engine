import json
import requests
from config import nyt_key

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

print(nyt_article_search("bitcoin"))