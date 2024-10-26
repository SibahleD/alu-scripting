#!/usr/bin/python3
"""Finding Number of subscribers in a given subreddit"""

import requests

"""Module"""

def number_of_subscribers(subreddit):
    response = requests.get("https://www.reddit.com/r/{}.json".format(subreddit))
    json_response = response.json
    print(json_response['data']['subscribers'])
