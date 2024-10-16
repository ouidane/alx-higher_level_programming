#!/usr/bin/python3
"""Define a class_to_join class"""
import json


def to_json_string(my_obj):
    """
    Convert a Python object into its JSON representation as a string.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
