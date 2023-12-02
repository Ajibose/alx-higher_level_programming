#!/usr/bin/python3
"""
    sends a post request to a url
"""
import urllib.request
import urllib.parse
import sys


def post_content(url, email):
    """post email to url"""
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        return response.read



if __name__ == '__main__':
    post_content(sys.argv[1], sys.argv[2])
