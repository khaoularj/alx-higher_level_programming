#!/usr/bin/python3
""" define a new class called Rectangle """
from models.base import Base


class Rectangle(Base):
    """this class inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """this is the class constructor
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: the horizontal position of the rectangle
            y: the vertical position of the rectangle
            id: id of the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, val):
        """this is the setter of the width of the rectangle"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """getter of the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, val):
        """this is the setter of the height of the rectangle"""
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """getter of the horizontal position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, val):
        """this is the setter of the horizontal position of the rectangle"""
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """getter of the horizontal vertical position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, val):
        """this is the setter of the vertical position of the rectangle"""
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """ adding the public method that returns
        the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print()
            """for i in range(self.height):
            for k in range(self.width):
                print('#', end='')
            print()"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """overriding the __str__ method so that
        it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update the public method that assigns an argument to each attribute
        Args:
            *args: new positional argument
                1st args represent id
                2nd args represent width
                3rd args represent height
                4th args represent x
                5th args represent y
            **kwargs: keyword arguments as a dictionary
        """
        attr = ["id", "width", "height", "x", "y"]
        for j in range(len(args)):
            if j < len(attr):
                setattr(self, attr[j], args[j])

        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)

    def to_dictionary(self):
        """adding the public method that returns
        the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
