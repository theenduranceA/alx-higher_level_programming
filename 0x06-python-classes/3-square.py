#!/usr/bin/python3
"""A class defining a square."""


class Square():
    """A square class."""

    def __init__(self, size=0):
        """Initializating the class square."""

        if type(size) != int:
            """Size is a private instance attribute."""

            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area."""
        return self.__size ** 2
