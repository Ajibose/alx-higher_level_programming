#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list.

    Args:
        my_list(list): List whose element to delete
        idx(int): position of the element to delete

    Return:
        returns new list containing all element of my_list except the element
            deleted
    """

    if not my_list:
        return None

    if idx >= len(my_list) or idx < 0:
        return my_list

    del my_list[idx]
    return (my_list)
