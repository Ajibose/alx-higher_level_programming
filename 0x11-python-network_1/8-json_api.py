#!/usr/bin/python3
"""
    sends a post request
"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) < 2:
        val = ""
    else:
        val = sys.argv[1]

    req = request.post(url, data={'q': val})
    return req.text
