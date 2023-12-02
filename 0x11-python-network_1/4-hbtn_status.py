#!/usr/bin/python3
"""
    Sends a request to a url
"""
import requests


def make_connection(url):
    """fetches https://alx-intranet.hbtn.io/status"""
    req = requests.get(url)
    return req.text


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    content = make_connection(url)
    print(f"Body response:\n\t- type: {type(content)}\n\t- content: {content}")
