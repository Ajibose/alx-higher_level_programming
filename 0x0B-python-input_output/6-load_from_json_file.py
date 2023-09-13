#!/usr/bin/python3
"""Deserialize a python object from a text file"""


import json


def load_from_json_file(filename):
    """creates an Object from a JSON file

    Args:
        filename: path to file to read from

    """
    with open(filename, 'r', encoding="utf-8") as f:
        obj = json.load(f)

    return obj
