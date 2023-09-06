#!/usr/bin/python3
"""5-text_indentation.py"""


def text_indentation(text):
    """Prints a text with 2 new linesi when encounter ":?."
    Args:
        text(str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    characters = ".?:"
    if not isinstance(text, str):
        raise TypeError("text must be string")

    for ch in text:
        print(ch, end='')
        if ch in characters:
            print("\n")
