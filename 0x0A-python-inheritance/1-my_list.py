#!/usr/bin/python3
"""Define a list class"""

class MyList(list):
    """Subclass of list"""
    def __init__(self):
        """Initialize the list"""
        super().__init__()

    def print_sorted(self):
        """Print a sorted list"""
        ascended_list = sorted(self)
        print(ascended_list)
