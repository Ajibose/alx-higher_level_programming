#!/usr/bin/python3
"""
    Sends a request to a url and
    displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys


def make_connection(url):
    """fetches https://alx-intranet.hbtn.io/status"""
    req = requests.get(url)
    return req.headers


if __name__ == '__main__':
    url = sys.argv[1]
    headers = make_connection(url)
    if 'X-Request-Id' in headers:
        print(headers['X-Request-Id'])
