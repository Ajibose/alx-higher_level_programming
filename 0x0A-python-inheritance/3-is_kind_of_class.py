#!/usr/bin/python3
"""Check the instance of a object"""


def is_kind_of_class(obj, a_class):
    """ Check if obj is an instance of, or
        if the object is an instance of a class that inherited from a_class

    Return:
        return True on success, otherwise False

    """
    return isinstance(obj, a_class)
