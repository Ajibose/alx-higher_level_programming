#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element at index idx

    Args:
        my_list(list): The list of integers whose element to retrieve
        idx(int): index of element to recieve

    Return:
        retturns element at index idx
    """
    if idx < 0:
        return None

    elif idx >= len(my_list):
        return None
    
    return my_list[idx]
