#!/usr/bin/python3
"""Defines a class that inherits from int class"""


class MyInt(int):
    """Invert the behaviour == and != operators"""
    def __eq__(self, obj):
        return super().__ne__(obj)

    def __ne__(self, obj):
        return super().__eq__(obj)
