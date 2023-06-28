#!/usr/bin/python3
"""Magic class replicating a python bytecode."""


import math
"""Import module."""


class MagicClass:
    """Magic class"""

    def __init__(self, radius=0):
        """Initializing the class."""
        if type(radius) not in (int, float):
            raise TypeError('radius must be a number')
        self.radius = radius

    def area(self):
        """Public instance method, returns area of class"""
        return self.radius ** 2 * math.pi

    def circumference(self):
        """Public instance method, returns circumference of class"""
        return 2 * math.pi * self.radius
