#!/usr/bin/python3
"""Defines a function that writes a tring to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file

    Args:
        fileame(str, optional): path to file to write to
        text(str, optional): string to write

    Return:
        returns the number of charceter written

    """

    with open(filename, 'w', encoding="utf-8") as f:
        ch = f.write(text)

    return ch
