import json
import requests
from config import cryptocontrol_key
from crypto_news_api import CryptoControlAPI

api = CryptoControlAPI(cryptocontrol_key)

def get_crypto_control_top_news():
    res = {}
    topNews = api.getTopNews()
    index = 0

    for entry in topNews:
        res[index] = {
            "title" : entry["title"],
            "description" : entry["description"],
            "url" : entry["url"],
            "source" : entry["sourceDomain"],
            "coins" : [coin["name"] for coin in entry["coins"]]
        }
        index+=1
    return res

get_crypto_control_top_news()

def get_cryptopanic_latest(ticker):
    url = 'https://cryptopanic.com/api/v1/posts/?auth_token=f21d6681cc7f5638d2ac3006377811ff433a4833&currencies={}&public=true'.format(ticker)

    response = requests.get(url)
    response = json.loads(response.text)
    results = response["results"]

    index = 0
    dic = {}

    for post in results:
        dic[index] = post
        index+=1

    return dic
