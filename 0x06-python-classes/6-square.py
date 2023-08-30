#!/usr/bin/python3
"""This module defines a class that is based on the module '4-square.py'
    The class furthermore contain an instantiation method and computes the area
    print the area

Example:
    $ s = Square(2)
    $ s.area() # also Square.area(s)
        4
    $ s.my_print() # alse Square.area(s)
"""


class Square:
    """This class initializes a class

    Attribute:
        size(int): The size of the Square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """class Square Init method

        Args:
            size(int, optional): size to make square object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """self.size getter and setter property"""
        return (self.__size)

    @property
    def position(self):
        """position getter and setter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(num, int) for num in value) or not all(
                        num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Computes the area the Square object

        Return:
            return value, the square object area
        """
        area = self.__size ** 2
        return (area)

    def my_print(self):
        """Prints the square"""
        if (self.__size == 0):
            print("")

        for i in range(self.__position[1]):
            print("")
        for i in range(1, self.__size + 1):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(1, self.__size + 1):
                print("#", end="")
            print("")
