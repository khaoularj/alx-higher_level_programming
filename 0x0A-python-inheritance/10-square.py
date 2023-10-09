#!/usr/bin/python3
"""define a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this is the Square class"""
    def __init__(self, size):
        """defining a new constructor
        Args:
            size: size of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
