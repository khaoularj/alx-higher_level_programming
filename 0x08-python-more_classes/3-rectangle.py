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

    def area(self):
        """Return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ returns a nicely printable string representation of an instance
        and print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        rectangle = []
        for element in range(self.__height):
            [rectangle.append('#') for items in range(self.__width)]
            if element != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
