#!/usr/bin/python3
"""
    Defines a class based on 1-rectangle.py
"""


class Rectangle:
    """A class that creates a rectangle

    Attributes:
        width(int): width of the rectangle
        height(int): height of the rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instatiate the rectangle object"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        """Print the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            rect = []
        else:
            rect = [["#" for j in range(self.__width)] for i in range(
                self.__height)]
        return "\n".join(["".join(row) for row in rect])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

        if not value >= 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if not value >= 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Computes the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of the rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__height + self.__width)
