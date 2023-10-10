#!/usr/bin/python3
"""Function to query a list of all hot posts on a given
 Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Base case: if after is None, there are no more
    pages, so return the hot_list"""
    if after is None:
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    x = {
        "User-Agent": "Your_User_Agent"
    }
    p = {
        "limit": 25,
        "after": after
    }

    z = False

    try:
        response = requests.get(url, headers=x, params=p, allow_redirects=z)

        if response.status_code == 200:
            data = response.json().get("data")
            if data:
                after = data.get("after")
                children = data.get("children")
                for child in children:
                    title = child.get("data").get("title")
                    hot_list.append(title)

                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        elif response.status_code == 404:
            return None
        else:
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
