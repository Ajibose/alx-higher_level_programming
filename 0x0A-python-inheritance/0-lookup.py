#!/usr/bin/python3
"""Defines a function that returns the list of available
    attributes and methods of an object:"""


def lookup(obj):
    """Get the all attribute and methods of an object

    Return:
        Return the list of the attriutes and methods

    """
    if not obj:
        return

    return dir(obj)
