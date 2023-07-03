#!/usr/bin/python3
"""A rectangle class module."""


class Rectangle:
    """A class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Instantiation of the class rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """To get the size of the rectangle.
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
        """To get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """To set the height of the rectangle.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """The perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
