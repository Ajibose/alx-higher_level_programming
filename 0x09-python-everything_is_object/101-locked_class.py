#!/usr/bin/pyhton3
"""A locked class"""


class LockedClass():
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        super().__setattr__(name, value)
