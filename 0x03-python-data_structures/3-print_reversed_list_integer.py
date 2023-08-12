#!/usr/python3

def print_reversed_list_integer(my_list=[]):
    """
    Reveres a list

    Args:
        my_list(list): list to reverse

    Return: None
    """

    for  i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
