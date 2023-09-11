#!/usr/bin/python3
"""101-add_attribute.py"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object if its possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
