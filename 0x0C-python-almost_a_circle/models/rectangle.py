#!/usr/bin/python3
"""Module for class Rectangle."""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the size if the Rectangle."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Sette the width of the Rectangle."""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Gets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the Rectangle."""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter function for x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter function for x."""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter function for y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter function for y."""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Rectangular area that returns the
        area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Public method that prints in stdout."""
        y = self.__y
        height = self.__height
        x = self.__x
        width = self.__width
        for i in range(y):
            print()
        for i in range(height):
            print(" " * x, end="")
            print("#" * width)

    def __str__(self):
        """Creates a new string."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Public method that ssigns an argument to each attribute"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for u, v in kwargs.items():
                if hasattr(self, u):
                    setattr(self, u, v)

    def to_dictionary(self):
        """Public method that returns the
        dictionary representation of Rectangle."""
        dictionary = {}

        for u, v in self.__dict__.items():
            keys = u.split("__")[-1]
            dictionary[keys] = v
        return dictionary
