#!/usr/bin/python3
"""Defining a new class Rectangle that define a rectangle"""


class Rectangle:
    """this is the new class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """get the width of the rectangle"""
        type_error = "width must be an integer"
        value_error = "width must be >= 0"
        if not isinstance(value, int):
            raise TypeError(type_error)
        if value < 0:
            raise ValueError(value_error)
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the hight of the rectangle"""
        type_errormsg = "height must be an integer"
        value_errormsg = "height must be >= 0"
        if not isinstance(value, int):
            raise TypeError(type_errormsg)
        if value < 0:
            raise ValueError(value_errormsg)
        self.__height = value
