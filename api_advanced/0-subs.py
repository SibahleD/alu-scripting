#!/usr/bin/python3

"""
Finding Number of subscribers in a given subreddit
"""

import requests

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def number_of_subscribers(subreddit):
    """Finding Number of subscribers in a given subreddit"""
    response = requests.get(f'https://www.reddit.com/r/{subreddit}.json', headers=headers)
    json_response = response.json
    print(json_response['data']['subscribers'])
