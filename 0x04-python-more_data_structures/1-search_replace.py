#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list.

    Args:
        my_list(list): list whose element to replace
        serach: element to replace
        replace: what to replace search

    Return:
        retur new list with search replaced with replace
    """
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
