#!/usr/bin/python3

"""
recuse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": "100", "after": after}
    response = requests.get(url, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        hot_list.append(post["data"]["title"])

    after = response.json().get("data", {}).get("after", None)

    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
