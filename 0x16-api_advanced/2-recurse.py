#!/usr/bin/python3
"""Function that query the list of all hot_posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns the_list of titles of all hot_posts on a given subreddit."""
    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    api_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    api_response = requests.get(api_url, headers=api_headers, params=params,
                            allow_redirects=False)
    if api_response.status_code == 404:
        return None

    results = api_response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for x in results.get("children"):
        hot_list.append(x.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list