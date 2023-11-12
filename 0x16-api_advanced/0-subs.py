#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return total_numbers of subscribers on a given subreddit."""
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    api_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    api_response = requests.get(api_url, headers=api_headers, allow_redirects=False)
    if api_response.status_code == 404:
        return 0
    results = api_response.json().get("data")
    return results.get("subscribers")