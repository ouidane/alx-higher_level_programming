#!/usr/bin/python3
"""Define a load_from_json_file"""


import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The object loaded from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
