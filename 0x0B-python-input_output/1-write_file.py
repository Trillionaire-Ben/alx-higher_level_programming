#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)

    Args:
        filename (str): filename
        text (str): text to be written
    Returns:
        The number of characters written.
    """
    with open("{}".format(filename), 'w', encoding="utf-8") as f:
        return f.write(text)
