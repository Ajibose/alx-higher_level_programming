#!/usr/bin/python3
"""
    Defines a class that creates a rectangle
"""


class Rectangle:
    """A class that creates a rectangle"""
    def __init__(self, width=0, height=0):
        """Instatiate the rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Attribute width setter and getter property"""
        return self.__width

    @property
    def height(self):
        """Attribute height setter and getter property"""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__height = value
