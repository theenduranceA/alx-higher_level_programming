#!/usr/bin/python3
"""Module for read_file."""


def read_file(filename=""):
    """Function that reads a text file"""
    with open(filename, 'r') as f:
        read_data = f.read()
    print(read_data, end="")
