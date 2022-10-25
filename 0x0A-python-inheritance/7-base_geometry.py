#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""
    
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """fn that validates value

        Args:
            name (str): string value
            value (int): integer params
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
