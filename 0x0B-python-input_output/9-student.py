#!/usr/bin/python3
"""Student to JSON """


class Student:
    """CLASS THAT DEFINES A STUDENT"""

    def __init__(self, first_name, last_name, age):
        """Instantiation

        Args:
            first_name (str): name
            last_name (str): name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
