#!/usr/bin/python3
"""Deserialize a python data object"""


import json


def from_json_string(my_str):
    """Gets an object (Python data structure) represented by a JSON string:

    Args:
        my_str: the object to serialize

    Return:
        returns pytho data representation of my_str

    """
    return json.loads(my_str)
