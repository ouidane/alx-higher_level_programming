#!/usr/bin/python3
"""Define a class_to_join class"""


def class_to_json(obj):
    """
    Convert an object with serializable attributes to
    a dictionary for JSON serialization.

    Args:
        obj (object): An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object with
        serializable attributes.
    """
    if hasattr(obj, '__dict__'):
        serializable_attrs = {}
        for key, value in obj.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serializable_attrs[key] = value
        return serializable_attrs
    return {}
