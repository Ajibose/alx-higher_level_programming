#!/usr/bin//python3

def print_list_integer(my_list=[]):
    """output all integers of a list

    Args:
        my_list(list): list whose element to output

    Return:
        returns None
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
