#!/usr/bin/python3
"""Check the type of a object"""


def is_same_class(obj, a_class):
    """ Check if obj is exactly an instance of a_class

    Return:
        return True on success, otherwise False

    """
    if obj.__class__ == a_class:
        return True

    return False
