#!/usr/bin/python3
"""A rectangule class module."""


class Rectangle:
    """An class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Instantiation the class rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """To retrieve the size of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """"To set the size of the rectangle.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """To set the size of the rectangle.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
