#!/usr/bin/python3
"""Module for Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits from rectangle"""

    def __init__(self, size):
        """Initializing the size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the s<F11>quare"""
        return self.__size ** 2
