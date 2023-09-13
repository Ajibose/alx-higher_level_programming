#!/usr/bin/python3
"""Serialize a python object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj(object): object to serialize
        filename: path to file to write to

    """
    with open(filename, 'a', encoding="utf-8") as f:
        json.dump(my_obj, f)
