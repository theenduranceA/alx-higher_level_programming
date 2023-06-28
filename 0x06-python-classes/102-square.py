#!/usr/bin/python3
"""A class defining a square."""


class Square():
    """A square class."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializating the class square."""

        self.size = size
        """Size is a private instance attribute."""
        self.position = position
        """Position is a private instance attribute."""

    def area(self):
        """Public instance method, returns the current area of the Square."""
        return self.__size ** 2

    @property
    def size(self):
        """To retrieve the size of the Square"""
        return self.__size

    @size.setter
    def size(self, SizeVal):
        """To set the size of the Square"""
        if type(SizeVal) != int:
            raise TypeError("size must be an integer")
        if SizeVal < 0:
            raise ValueError("size must be >= 0")
        self.__size = SizeVal

    def __eq__(self, other):
        """Square equals square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Square not equals square area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Square is greater than square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Square is greater than or equal to square area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Square is less than square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Square is less than or equal to square area."""
        return self.area() <= other.area()
