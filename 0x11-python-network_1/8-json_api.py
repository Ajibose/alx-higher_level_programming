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

    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data={'q': val})
    
    try:
        content_dict = eval(req.text)
    except Exception:
        print("Not a valid JSON")
    
    if type(content_dict) != dict:
        print("Not a valid JSON")
    elif not content_dict:
        print("No result")
    else:
            print(f"[{content_dict['id']}] {content_dict['name']}")
