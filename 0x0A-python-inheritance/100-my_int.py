#!/usr/bin/python3

"""Module for MyInt."""


class MyInt(int):
    """MyInt class that inherit from int"""

    def __ne__(self, other):
        return int(self) == int(other)

    def __eq__(self, other):
        return int(self) != int(other)
