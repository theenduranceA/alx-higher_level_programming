#!/usr/bin/python3
"""A class defining a square."""


class Square():
    """A square class."""

    def __init__(self, size=0):
        """Initializating the class square."""

        self.__size = size
        """Size is a private attribute."""

    def area(self):
        """Public instance method, returns the current area of the Square."""
        return self.__size ** 2

    @property
    def size(self):
        """To retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, Val):
        """To set the size of the Square."""

        if type(Val) is not int:
            raise TypeError("size must be an integer")
        if Val < 0:
            raise ValueError("size must be >= 0")
        self.__size = Val

    def my_print(self):
        """Prints the Square."""

        size = self.__size
        if size == 0:
            print("")
            return
        for x in range(size):
            for y in range(size):
                print("#", end="")
            print("")
