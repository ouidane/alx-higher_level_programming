#!/usr/bin/python3
"""
This module provides a function to determine if an object is an exact instance 
of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Determines whether the given object is exactly an instance of the specified class.

    Args:
        obj (any): The object whose class is to be checked.
        a_class (type): The class to compare the object's type against.

    Returns:
        bool: True if the object is exactly an instance of the specified class, 
              False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
