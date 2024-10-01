#!/usr/bin/python3

"""This module defines a class Square"""


class Square:
    """A class that defines a square"""
    
    def __init__(self, size=0):
        """
        Initializes a square with the given size

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square"""
        return self.__size ** 2
