#!/usr/bin/python3
"""defining a Square class"""


class Square:
    """representing a square class"""
    def __init__(self, size=0):
        """ Initializing a new square
        Args:
            size (int): The size of the square"""
        type_error_msg = "size must be an integer"
        value_error_msg = "size must be >= 0"
        if not isinstance(size, int):
            raise TypeError(type_error_msg)
        elif size < 0:
            raise ValueError(value_error_msg)
