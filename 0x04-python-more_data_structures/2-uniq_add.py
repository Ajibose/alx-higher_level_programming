#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer).

    Args:
        my_list(list): list to sum

    Return:
        return sum of all element in my_list
    """
    if not my_list:
        return (0);

    total = __import__('functools').reduce(lambda x, y: x + y, set(my_list))
    return (total)
