#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """A function that appends a string to a text file (UTF8)

    Args:
        filename (str): filename
        text (str): text to be written
    Returns:
        The number of characters written.
    """
    with open("{}".format(filename), 'a', encoding="utf-8") as f:
        return f.write(text)
