#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces the element at position idx of my_list not modifying the original list

    Args:
        my_list(list): list to modify
        idx(int): index of elemsnt to modify
        element: value to change to

    Returns:
        modified list on success, None on failure
    """

    if my_list is None:
        return None

    new_list = []
    for i in range(len(my_list)):
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[i])

    return new_list
