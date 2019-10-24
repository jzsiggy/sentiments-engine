import json
import requests

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

get_cryptopanic_latest("BTC")