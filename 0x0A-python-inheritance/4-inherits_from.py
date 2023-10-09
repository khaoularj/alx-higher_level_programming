#!/usr/bin/python3
"""define a fun that checks if the object is an instance of a class
that inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """"this function checks if it's an instance or not

    Args:
        obj:the checked object
        a_class: the specified class
    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False"""
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
