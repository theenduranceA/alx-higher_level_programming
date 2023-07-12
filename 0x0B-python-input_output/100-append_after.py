#!/usr/bin/python3
"""Module for append_after."""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file."""
    insert = ""
    with open(filename) as r:
        for line in r:
            insert = insert + line
            if search_string in line:
                insert = insert + new_string
    with open(filename, "w") as w:
        w.write(insert)
