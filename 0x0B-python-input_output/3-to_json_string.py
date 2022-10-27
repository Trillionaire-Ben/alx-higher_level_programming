#!/usr/bin/python3
"""To JSON string """
import json


def to_json_string(my_obj):
    """fn that returns the JSON representation of an object

    Args:
        my_obj (str): string object
    Returns:
        returns the JSON representation of an object
    """
    return json.dumps(my_obj)
