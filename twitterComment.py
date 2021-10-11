# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:19:16 2021

@author: 20380
"""

import requests

# credential
bearer_token = "REPLACE_WITH_KEY"

def getTwitterComments(school_name):
    url = "https://api.twitter.com/2/tweets/search/recent?query="
    url = url + school_name +'&tweet.fields=created_at'

    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    res_json = response.json()
    print(res_json['data'][0]['text'])