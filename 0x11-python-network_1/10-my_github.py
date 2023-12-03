#!/usr/bin/python3
"""
    Display my id using the Github API
"""
import sys
import requests


if __name__ == '__main__':
    user = sys.argv[1]
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {sys.argv[2]}",
            "X-GitHub-Api-Version": "2022-11-28"}

    url = f"https://api.github.com/{user}"
    response = requests.get(url, headers=headers)
    if not response:
        print("None")
    else:
        print(response.json["id"])
