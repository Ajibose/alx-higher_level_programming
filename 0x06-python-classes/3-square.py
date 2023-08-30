#!/usr/bin/python3
"""This module defines a class that is based on the module '2-square.py'
    The class furthermore contain an instantiation method and computes the area

Example:
    $ s = Square(2)
    $ s.area() # also Square.area(s)
        4
"""


class Square:
    """This class initializes a class

    Attribute:
        size(int): The size of the Square object
    """
    def __init__(self, size=0):
        """class Square Init method

        Args:
            size(int, optional): size to make square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Computes the area the Square object

        Return:
            return value, the square object area
        """
        area = self.__size ** 2
        return (area)
