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