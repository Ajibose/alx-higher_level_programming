#!/usr/bin/python3
"""Defines a function that appends to the end of a text file"""


def append_write(filename="", text=""):
    """Appends to the end of a file using UTF8 encoding

    Args:
        filename(str, optional): path to file to write to
        text(str, optional): string to append to file

    Return:
        returns the number of character written to filename

    """
    with open(filename, 'a', encoding="utf-8") as f:
        ch = f.write(text)

    return ch
