# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:19:16 2021

@author: Mark He
"""

import requests

# credential
bearer_token = "AAAAAAAAAAAAAAAAAAAAALw%2FTwEAAAAA5mGzkkQRzM5lUExaBkZDfYbS3Y0%3DwqRFpCaqzANZn3kiEwO85WoxjE5PAsQ54tSokCZFvPZy0zI2JT"

# Get the top twitter comment from twitter through API
def getTwitterComments(school_name):
    url = "https://api.twitter.com/2/tweets/search/recent?query="
    url = url + school_name + '&tweet.fields=created_at'

    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    if response is None:
        print("No tweets for "+school_name)
    else:
        try:
            res_json = response.json()
            print(res_json['data'][0]['text'])
        except:
            print("No tweets for "+school_name)