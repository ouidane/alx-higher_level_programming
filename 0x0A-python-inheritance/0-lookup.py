#!/usr/bin/python3
"""
This module defines a function to retrieve all attributes and methods of an object.
It uses the built-in dir() function to achieve this.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of the given object.

    Args:
        obj: The object whose attributes and methods are to be retrieved.

    Returns:
        A list containing the names of the attributes and methods of the object.
    """
    attr_and_methods = dir(obj)
    return attr_and_methods
