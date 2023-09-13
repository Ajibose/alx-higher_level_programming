#!/usr/bin/python3
"""100-append_after.py"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after encountering a string in a line

    Args:
        filename(str): path to file
        search_string(str): string to search
        new_string(str): string to write

    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
