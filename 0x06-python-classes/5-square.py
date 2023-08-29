#!/usr/bin/python3
"""defining a Square class"""


class Square:
    """representing a square class"""
    def __init__(self, size):
        """ Initializing a new square
        Args:
            size (int): The size of the square"""
        self.size = size

    @property
    def size(self):
        """size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        type_error_msg = "size must be an integer"
        value_error_msg = "size must be >= 0"
        if not isinstance(value, int):
            raise TypeError(type_error_msg)
        elif value < 0:
            raise ValueError(value_error_msg)
        self.__size = value

    def area(self):
        """calculate the square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # char"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
