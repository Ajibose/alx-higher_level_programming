#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggest integer of a list.

    Args:
        my_list(list): The list

    Return:
        returns None if the list is empty otherwise the list max element
    """
    if not my_list:
        return None

    maxim = my_list[0]
    for i in my_list:
        if maxim < i:
            maxim = i
    return (maxim)
