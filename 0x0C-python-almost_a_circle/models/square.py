#!/usr/bin/python3
"""Module of square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square that Inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.width = value

    def update(self, *args, **kwargs):
        """Public method that ssigns an argument to each attribute"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for u, v in kwargs.items():
                if hasattr(self, u):
                    setattr(self, u, v)

    def __str__(self):
        """Creates a new string and returns tge attributes."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    def to_dictionary(self):
        """Public method that returns Dictionary representation of Square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
