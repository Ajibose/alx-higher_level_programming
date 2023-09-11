#!/usr/bin/python3
"""Check the instance of a object"""


def inherits_from(obj, a_class):
    """ Check if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class

    Return:
        return True on success, otherwise False

    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
