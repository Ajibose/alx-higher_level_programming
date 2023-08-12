#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all characters c and C from a string.

    Args:
        my_string(str): string to modify

    Returns:
        Return a new modified string
    """

    if my_string is None:
        return None

    new_string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch

    return new_string
