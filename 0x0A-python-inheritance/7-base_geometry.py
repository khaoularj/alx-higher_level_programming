#!/usr/bin/python3
"""Define an empty class"""


class BaseGeometry:
    """this is the new class"""
    def area(self):
        msg = "area() is not implemented"
        raise Exception(msg)

    def integer_validator(self, name, value):

        msg1 = ("{} must be an integer".format(name))
        msg2 = ("{} must be greater than 0".format(name))
        if type(value) != int:
            raise TypeError(msg1)
        if value <= 0:
            raise ValueError(msg2)
