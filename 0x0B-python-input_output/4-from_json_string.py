#!/usr/bin/python3
"""From JSON string to Object """
import json


def from_json_string(my_str):
    """fn that returns an object (Python data structure)

    Args:
        my_str (str): string object
    Returns:
        returns an object (Python data structure)
    """
    return json.loads(my_str)
