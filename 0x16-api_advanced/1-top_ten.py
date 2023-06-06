#!/usr/bin/python3
"""
Created on Tue Jun 16 13:09:53 2023

@author: Alfred Ternor
"""
from json import loads
from requests import get


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/alfy_)"
    }
    response = get(url, headers=headers, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
    except:
        print('None')
