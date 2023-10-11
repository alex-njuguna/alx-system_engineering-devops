#!/usr/bin/python3
"""Function to query a list of all hot posts on a given
 Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    """Recursively queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.

    Args:
    subreddit: The name of the subreddit to query.
    hot_list: A list to store the titles of the hot articles.

    Returns:
    A list containing the titles of all hot articles for the given subreddit,
    or None if no results are found.
    """

    """Make a request to the Reddit API."""
    response = requests.get(
        f"https://oauth.reddit.com/r/{subreddit}/hot.json",
        headers={"Authorization": "Bearer YOUR_REDDIT_API_TOKEN"},
    )

    """Check if the request was successful."""
    if response.status_code == 200:
        """Parse the JSON response."""
        data = response.json()

    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])

    if data["data"]["after"]:
        return recurse(subreddit, hot_list)
    else:
        return None

    return hot_list
