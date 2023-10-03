#!/usr/bin/python3
"""defining the function that adds two int
Args:
    first_name: The first name to print.
    last_name: The last name to print.
"""


def add_integer(a, b=98):
    """this function return the addition of two numbers
    Raises:
        TypeError: If either of first_name or last_name are not strings"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a)+(b))
