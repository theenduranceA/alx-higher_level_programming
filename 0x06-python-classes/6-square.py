#!/usr/bin/python3
"""A class defining a square."""


class Square:
    """A square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializating the class square."""

        self.__size = size
        """Size is a private instance attribute."""
        self.__position = position
        """Position is a private instance attribute."""

    def area(self):
        """Public instance method, returns the current area of the Square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square."""

        size = self.__size
        position = self.__position
        if size == 0:
            print()
            return
        for i in range(position[1]):
            print()
        for j in range(size):
            for x in range(position[0]):
                print(" ", end="")
            for y in range(size):
                print("#", end="")
            print()

    @property
    def size(self):
        """To retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, size):
        """To set the size of the Square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """To retrieve the position of the Square."""
        return self.__position

    @position.setter
    def position(self, position):
        """To set the position of the Square."""
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(val) != int for val in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(val < 0 for val in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
