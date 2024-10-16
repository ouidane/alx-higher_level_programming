#!/usr/bin/python3
"""Define a save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the JSON file.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
