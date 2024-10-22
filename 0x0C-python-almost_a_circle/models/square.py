#!/usr/bin/python3
"""Define a Square class that inherite of Rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class represents a square, inheriting from Rectangle

    Attributes:
        Inherits attributes from Rectangle:
        - __width (int): The width of the square.
        - __height (int): The height of the square.
        - __x (int): The horizontal position of the square.
        - __y (int): The vertical position of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The horizontal position of the
            square (default is 0).
            y (int, optional): The vertical position of the
            square (default is 0).
            id (int, optional): An optional integer ID (default is None)

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
