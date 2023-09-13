#!/usr/bin/python3
"""Technical interview preparation question @ALX SoFTWARE ENGINEERING"""


def pascal_triangle(n):
    """Computes the pascal triangle of n

    Args:
        n(int): no of pascal rows to calculate

    Return:
        returns list of lists of integers representiong the pascal triangle

    """
    new_list = []

    if n <= 0:
        return new_list

    for i in range(n):
        new_list.append([])
        new_list[i].append(1)
        for j in range(i):
            if i > 1 and j != 0:
                second = new_list[i - 1][j - 1] + new_list[i - 1][j]
                new_list[i].append(second)
            if (j == i - 1):
                new_list[i].append(1)
        i += 1

    return new_list
