import json
import requests
from config import guardian_key

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

guardian_search("BTC")