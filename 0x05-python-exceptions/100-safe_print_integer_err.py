#!/usr/bin/python3

def safe_print_integer_err(value):
    """ prints an integer."""

    import os

    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        os.write(2, str.encode("Exception: {}\n".format(e)))
        return False
