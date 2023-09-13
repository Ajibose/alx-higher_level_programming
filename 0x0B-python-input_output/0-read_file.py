#!/usr/bin/python3
"""Define a function that reads from a text file"""


def read_file(filename=""):
    """Reads from a text file using UTF8 encoding

    Args:
        filename(str): path to file to read from

    """
    if filename == "":
        return ""

    with open(filename, 'r', encoding="utf-8") as f:
        ch = f.read()

    print(ch, end="")
