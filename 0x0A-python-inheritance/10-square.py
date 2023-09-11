#!/usr/bin/python3
"""Define a class that inherit from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
