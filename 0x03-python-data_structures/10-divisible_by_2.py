#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds the multiples of 2 in a list

    Args:
        my_list(list): The list

    Return:
        returns new list containing True or False
         depending on if thee element at the position is a multiple of 2
    """
    if not my_list:
        return None

    new_list = []
    for i in my_list:
        if (i % 2) == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
