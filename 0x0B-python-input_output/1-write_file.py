#!/usr/bin/python3
"""Module for write_file."""


def write_file(filename="", text=""):
    """Function that writes a string to a UTF8 text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
