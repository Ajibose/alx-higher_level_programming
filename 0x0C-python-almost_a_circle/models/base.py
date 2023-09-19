#!/usr/bin/python3
"""Defines a Base model class"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the json string representation of an object"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs(list): list of instances who inherits of Base

        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                obj_list = [item.to_dictionary() for item in list_objs]

        f.write(Base.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not bool(json_string) or json_string is None:
            return "[]"

        return json.loads(json_string)
