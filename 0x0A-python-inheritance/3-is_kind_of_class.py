#!/usr/bin/python3
"""define fun that checks for the instance of the specified class
or the instance of a class that inherited from the specified class"""


def is_kind_of_class(obj, a_class):
    """ checks if it's an instance or inherited intance of a class

    Args:
        obj: the checked object
        a_class: the specified class
    Returns:
        True if the object is an instance
        or if the object is an instance of a class that inherited from
        the specified class
        else, return False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
