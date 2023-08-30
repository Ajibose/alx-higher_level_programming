#!/usr/bin/python3
"""This module defines a class that is based on the module '0-square.py'
    The class furthermore contain an initialization method

Example:
    $ s = Square()
"""


class Square:
    """This class initializes a class

    Attribute:
        size(int): The size of the Square object
    """
    def __init__(self, size):
        """class Square Init method

        Args:
            size(int, optional): size to make square object
        """
        self.__size = size
