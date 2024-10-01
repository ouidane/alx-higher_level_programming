#!/usr/bin/python3

"""Create a class"""


class Square:
    """Represente a square"""
    def __init__(self, size=0):
        """Initialize a square with a given size"""
        self.__size = size

    @property
    def size(self):
        """Getter method for size attr"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size.attr"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' symbol characters"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
