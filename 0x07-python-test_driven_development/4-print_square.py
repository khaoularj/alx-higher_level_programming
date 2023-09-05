#!/usr/bin/python3
"""defining a function that prints a square with the character #"""


def print_square(size):
    """this is the function that prints a square with #"""
    if not isinstance(size, int):
        error_msg1 = "size must be an integer"
        raise TypeError(error_msg1)
    if size < 0:
        value_error_msg = "size must be >= 0"
        raise ValueError(value_error_msg)
    if not isinstance(size, int) and size < 0:
        error_msg2 = "size must be an integer"
        raise TypeError(error_msg2)
    for i in range(size):
        for y in range(size):
            print("#", end="")
        print()
