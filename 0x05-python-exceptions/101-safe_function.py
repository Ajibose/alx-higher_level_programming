#!/usr/bin/python3

def safe_function(fct, *args):
    """ executes a function safely."""

    import os

    try:
        return fct(*args)
    except Exception as e:
        os.write(2, str.encode("Exception: {}\n".format(e)))
        return None
