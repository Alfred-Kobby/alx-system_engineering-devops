#!/usr/bin/python3
"""
Created on Tue Jun 16 13:09:53 2023

@author: Alfred Ternor
"""
from json import loads
from requests import get


def recurse(subreddit, hot_list=[]):
    """recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/alfy_)"
    }
    response = get(url, headers=headers, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for title in children:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    except:
        print(None)
        return 0
