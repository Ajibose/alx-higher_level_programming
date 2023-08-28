#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints the result."""

    x = None
    try:
        x = a / b
        return (x)
    except (ZeroDivisionError):
        return None
    finally:
        print("Inside result: {}".format(x))
