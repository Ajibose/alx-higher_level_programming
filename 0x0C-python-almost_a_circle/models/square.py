#!/usr/bin/python3
"""Defines a class that inherits from module `models.rectangle` Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id})"\
                f" {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes"""
        if not args and not kwargs:
            return
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for i, j in kwargs.items():
                if i in attributes:
                    setattr(self, i, j)

    def to_dictionary(self):
        """Get the dictionary representation of a Square"""
        my_dict = super().to_dictionary()
        size = my_dict["width"]
        del my_dict["width"]
        del my_dict["height"]
        my_dict["size"] = size

        return my_dict
