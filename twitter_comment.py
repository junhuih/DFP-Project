# -*- coding: utf-8 -*-
"""
@author: Yifan Cheng, Skylar Du, Yashash Gaurav, Mark He
"""
import requests

# credential
bearer_token = "REPLACE_WITH_YOUR_OWN"


# Get the top twitter comment from twitter through API
def get_twitter_comments(school_name):
    try:
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
                print(res_json['data'][1]['text'])
                print(res_json['data'][2]['text'])
            except:
                print("No tweets for "+school_name)
    except:
        print("Error fetching twitter comments! Please check your internet!")
