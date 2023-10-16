#!/usr/bin/python3
"""Define a new class called Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this new class inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """this is the class constructor
        Args:
            size: size of the square
            x: the horizontal position of the square
            y:the vertical position of the square
            id: id of the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of the size of the square"""
        return self.width

    @size.setter
    def size(self, val):
        """this is the setter of the size of the square"""
        self.width = val
        self.height = val

    def __str__(self):
        """overloading __str__ method should return
        [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.height))

    def update(self, *args, **kwargs):
        """adding the public method that assigns attributes
        Args:
            *args: new positional argument
                1st args represent id
                2nd args represent the size
                3rd args represent x
                4th args represent y
            **kwargs: keyword arguments as a dictionary"""
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, v in kwargs.items():
                setattr(self, key, v)

    def to_dictionary(self):
        """adding the public method that returns
        the dictionary representation of a square"""
        return {
            "id": self.id,
            "size": self.height,
            "x": self.x,
            "y": self.y
            }
