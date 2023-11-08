#!/usr/bin/python3
"""Function that print hot_posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    api_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    api_response = requests.get(api_url, headers=api_headers, params=params,
                            allow_redirects=False)
    if api_response.status_code == 404:
        print("None")
        return
    results = api_response.json().get("data")
    [print(x.get("data").get("title")) for x in results.get("children")]