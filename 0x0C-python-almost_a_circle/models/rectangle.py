#!/usr/bin/python3
"""Defines a class that is dericed from models.base.Base"""


from models.base import Base

class Rectangle(Base):
    """Represent the rectangle

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle class

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int):
            y(int):

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id})"\
                f" {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    @property
    def width(self):
        """width attribute getter and setter property"""
        return self.__width

    @property
    def height(self):
        """height attribute getter and setter property"""
        return self.__height

    @property
    def x(self):
        """x attribute getter and setter property"""
        return self.__x

    @property
    def y(self):
        """y attribute getter and setter property"""
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Compute the area of the Rectangle"""
        return self.__height * self.__width

    def display(self):
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Updates the recatngle fields"""
        if not args and not kwargs:
            return

        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for i, j in kwargs.items():
                if i in attributes:
                    setattr(self, i, j)

