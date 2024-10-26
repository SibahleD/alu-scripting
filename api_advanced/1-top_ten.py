#!/usr/bin/python3
"""Module for fetching top 10 hot post titles from a subreddit."""

import requests


def top_ten(sub):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(sub)
    headers = {"User-Agent": "subreddit-hot-posts-fetcher"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    posts = response.json()['data']['children']
    for post in posts:
        print(post['data']['title']) 
    posts = response.json().get("data", {}).get("children", [])
    for item in posts:
        print(item.get("data", {}).get("title", None))
