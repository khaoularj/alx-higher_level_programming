#!/usr/bin/python3
"""define a function that checks for the instance of the specified class"""


def is_same_class(obj, a_class):
    """this function checks if it's an instance or not

    Args:
        obj: the checked object
        a_class: the specified class

    Returns:
        True if the object is exactly an instance of the specified class
        otherwise False"""

    if type(obj) == a_class:
        return True
    else:
        return False
