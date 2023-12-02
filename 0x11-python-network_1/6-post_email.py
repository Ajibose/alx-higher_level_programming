#!/usr/bin/python3
"""
    sends a POST request to the passed URL
"""
import sys
import requests


def post_content(url, email):
    """"ends a POST request to the passed URL with the email as a parameter,"""
    value = {'email': email}
    req = requests.post(url, data=value)
    return req


if __name__ == '__main__':
    response = post_content(sys.argv[1], sys.argv[2])
    print(response.text)
