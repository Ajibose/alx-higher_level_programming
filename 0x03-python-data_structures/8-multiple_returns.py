#!/usr/bin/python3
def multiple_returns(sentence):
    """Get the length of a string and its first character.

    Args:
        sentence(str): The string

    Return:
        returns a tuple containing the string's first character and its length
    """

    first_ch = sentence[0] if sentence else None
    new_tuple = len(sentence), first_ch
    return (new_tuple)
