#!/usr/bin/python3
"""Module for read_file."""


def read_file(filename=""):
    """Function that reads a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
