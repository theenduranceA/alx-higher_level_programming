#!/usr/bin/python3
"""Module for class Rectangle."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initalizing tge size of tge rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangular area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns tge  string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
