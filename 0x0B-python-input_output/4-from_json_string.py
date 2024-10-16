#!/usr/bin/python3
"""Define a from_json_string function"""
import json


def from_json_string(my_str):
    """
    Convert a JSON string into a Python object

    Args:
        my_str (str): The JSON string to be converted

    Returns:
        object: The Python object repr by the JSON strg.
    """
    return json.loads(my_str)
