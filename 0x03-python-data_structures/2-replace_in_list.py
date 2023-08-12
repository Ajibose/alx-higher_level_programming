#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element at index idx

    Args:
        my_list(list): list whose element to replace
        idx(int): index of element to replace
        element: what to change to

    Returns:
        returns the original list if idx is out of range
            or a new list with element at idx changed
    """
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
        
    my_list[idx] = element
    return my_list
