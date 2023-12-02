#!/usr/bin/python3
"""
    sends a request to the URL and displays the body of the response
"""
import urllib.request
import sys


def connect_with(url):
    """sends a request to the URL and displays the body of the response"""
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return f"Error code: {e.code}"


if __name__ == '__main__':
    print(connect_with(sys.argv[1]))
