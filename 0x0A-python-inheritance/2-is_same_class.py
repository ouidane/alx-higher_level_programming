#!/usr/bin/python3
"""Exact same object."""


def is_same_class(obj, a_class) -> bool:
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        abj (object): Object For check.
        a_class (type): Class to compare the object.
    """
    return type(obj) is a_class