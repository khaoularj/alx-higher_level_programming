#!/usr/bin/python3
"""defining a function that prints My name is <first name> <last name>
Args:
    first_name (str): The first name to print.
    last_name (str): The last name to print.
"""


def say_my_name(first_name, last_name=""):
    """this is the function that prints full name
     Raises:
        TypeError: If either of first_name or last_name are not strings"""
    if not isinstance(first_name, str):
        error_msg1 = "first_name must be a string"
        raise TypeError(error_msg1)
    if not isinstance(last_name, str):
        error_msg2 = "last_name must be a string"
        raise TypeError(error_msg2)
    print("My name is {} {}".format(first_name, last_name))
