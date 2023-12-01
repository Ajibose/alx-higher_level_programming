#!/usr/bin/python3
"""
    Fetches the content of a webpage
"""
import urllib.request


def fetch_content(url):
    """Fetches alx-intranet.hbtn.io content"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.read()


if __name__ == '__main__':
    fetch_content('https://alx-intranet.hbtn.io/status')

