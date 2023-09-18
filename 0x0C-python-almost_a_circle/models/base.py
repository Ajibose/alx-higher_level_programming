#!/usr/bin/python3
"""Defines a Base model class"""


class Base():
    """Represent the base model

    This class will be the base of all other classes in this project(`0x0C`)

    Attributes:
        __nb_objects(int): No of instances of the class when argument is None
        id(int): Instance attribute

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class

        Args:
            id(int): The id of the new instance

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
