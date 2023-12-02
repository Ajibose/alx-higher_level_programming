#!/usr/bin/python3
"""
    sends a request to the URL and displays the body of the response.
"""
import sys
import requests


def send_request(url):
    """ sends a request to the URL and displays the body of the response."""
    req = requests.get(url)
    if (req.status_code > 400):
        return f"Error code: {req.status_code}"
    return req.text


if __name__ == '__main__':
    print(send_request(sys.argv[1]))
