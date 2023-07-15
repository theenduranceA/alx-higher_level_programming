#!/usr/bin/python3
"""Module for base class."""

import json
from os import path


class Base:
    """The class base."""
    __nb_objects = 0
    """Private class attribute."""

    def __init__(self, id=None):
        """Class constructoe."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
