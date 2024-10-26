#!/usr/bin/python3
"""Finding Number of subscribers in a given subreddit"""

import requests

"""Module"""


def number_of_subscribers(sub):
    headers = {"User-Agent": "subreddit-subscriber-counter"}
    url = "https://www.reddit.com/r/{}.json".format(sub)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    json_response = response.json
    try:
        return json_response['data']['subscribers']
    except (KeyError, IndexError):
        return 0
