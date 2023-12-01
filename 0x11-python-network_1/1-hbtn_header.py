#!/usr/bin/python3
"""
    displays the a variable of the a response
"""
import sys
import urllib.request


def get_requestId(url):
    """Get the X-Request-Id variable found in the header of the response."""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        responseHeader = response.info()
        return responseHeader.get('X-Request-Id')


if __name__ == '__main__':
    url = sys.argv[1]
    get_requestId(url)
