#!/usr/bin/python3
"""define a rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is the class rectangle"""
    def __init__(self, width, height):
        """this is the constructor
        Args:
            width:the width of the rectangle
            height:the height of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
