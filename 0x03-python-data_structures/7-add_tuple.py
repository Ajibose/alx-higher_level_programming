#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples

    Args:
        tuple_a(tuple): first tuple
        tuple_b(tiple): second tuple

    Return:
        returns the resultant tuple
    """
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if (len1 < 2):
        for i in range(2 - len1):
            tuple_a = tuple_a + (0,)
    elif (len2 < 2):
        for i in range(2 - len2):
            tuple_b = tuple_b + (0,)

    x1, y1 = tuple_a[0], tuple_a[1]
    x2, y2 = tuple_b[0], tuple_b[1]

    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return (new_tuple)
