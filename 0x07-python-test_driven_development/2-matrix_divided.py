#!/usr/bin/python3
"""2-matrix_divided.py"""


def matrix_divided(matrix, div):
    """Divide all elements of matrix by div"""

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        size = len(matrix[0])
        if len(lists) != size:
            raise TypeError("Each row of the matrix must have the same size")
        
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    sz = 0

    for lists in matrix:
        new_list.append([])
        for i in lists:
            res = round(i / div, 2)
            new_list[sz].append(res)
        sz += 1

    return new_list
