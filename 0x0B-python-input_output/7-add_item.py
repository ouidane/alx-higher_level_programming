#!/usr/bin/python3
"""Defines a save_to_json_file function"""


import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the JSON file.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The object loaded from the file.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    try:
        existing_data = load_from_json_file("add_item.json")
    except json.JSONDecodeError:
        existing_data = []

    for arg in sys.argv[1:]:
        existing_data.append(arg)

    save_to_json_file(existing_data, "add_item.json")
