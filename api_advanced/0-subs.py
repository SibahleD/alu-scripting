#!/usr/bin/python3
"""Finding Number of subscribers in a given subreddit"""

import requests

"""Module"""


def number_of_subscribers(sub):
    headers = {"User-Agent": "subreddit-subscriber-counter"}
    response = requests.get("https://www.reddit.com/r/{}.json".format(sub), headers=headers)
    if response.status_code != 200:
        return 0
    json_response = response.json
    try:
        return json_response['data']['children'][0]['data']['subreddit_subscribers']
    except (KeyError, IndexError):
        return 0