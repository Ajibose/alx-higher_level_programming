#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix(list): mtrix whose square to determine

    Return:
        return a new matrix with element te square of matrix element
    """
    new_matrix = list(list(map(
        lambda x: x ** 2, matrix_sub)) for matrix_sub in matrix)
    return (new_matrix)
