#!/usr/bin/python3
"""Define a list that inherits from list"""


class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        print(sorted(self))
