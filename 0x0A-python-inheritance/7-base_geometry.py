#!/usr/bin/python3
"""Define a class based on 6-base_geometry.py"""


class BaseGeometry():
    """A class that defines a method"""
    def area(self):
        """A method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
