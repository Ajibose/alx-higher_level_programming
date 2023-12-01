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
    content = fetch_content('https://alx-intranet.hbtn.io/status')
    print(
            f"Body response:\n\t- "
            f"type: {type(content)}\n\t- "
            f"content: {content}\n\t- "
            f"utf8 content: {content.decode()}"
            )
