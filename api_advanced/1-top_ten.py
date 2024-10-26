#!/usr/bin/python3
"""Module for fetching top 10 hot post titles from a subreddit."""

import requests


def top_ten(subreddit):
        headers = {"User-Agent": "subreddit-hot-posts-fetcher"}
        response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit), headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        json_response = response.json()
        try:
            posts = json_response['data']['children']
            for post in posts:
                print(post['data']['title'])
        except (KeyError, IndexError):
            print(None)
