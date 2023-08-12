#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
        Prints a matrix of integers.

    Args:
        matrix(list): matrix to print

    Return
        return None
    """
    if matrix is None:
        return None

    for i in matrix:
        for j in i:
            print("{:d}".format(j), end=" ")
        print("")
