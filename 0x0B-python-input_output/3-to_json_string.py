#!/usr/bin/python3
"""Serialize a python data object"""


import json


def to_json_string(my_obj):
    """Gets the SON representation of an object (string)

    Args:
        my_obj: the object to serialize

    Return:
        returns the json representatio of my_obj

    """
    return json.dumps(my_obj)
