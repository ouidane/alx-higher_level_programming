#!/usr/bin/python3


class Square:
    """
    A class that defines a square by its size.
    
    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        """
        Initializes a square with the given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
