#!usr/bin/python3
"""creating a square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ A class of Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
