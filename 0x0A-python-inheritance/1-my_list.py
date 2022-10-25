#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
