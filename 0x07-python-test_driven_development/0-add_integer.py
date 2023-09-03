#!/usr/bin/python3
"""defining the function thhat adds two int"""


def add_integer(a, b=98):
    """this function return the addition of two numbers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a)+(b))
