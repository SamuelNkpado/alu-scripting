#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "python:subreddit.topten:v1.0 (by /u/fake_username)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        return

