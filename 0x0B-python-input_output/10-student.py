#!/usr/bin/python3
"""9-student.py"""


class Student():
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Return the dictionary representation of the class"""
        if type(attr) == list:
            new_dict = {}
            for key in attr:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

        return self.__dict__
