#!/usr/bin/python3
"""Module for Rectangle."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class of square tgat inherits from Rectangle."""

    def __init__(self, width, height):
        """Initalizing the size."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
