#!/usr/bin/python3
"""Define a Base class"""

import csv
import turtle
import json


class Base:
    """
    Base class represents the base of all classes.

    Attributes:
        __nb_objects (int): The number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): An optional integer ID (default is None).

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list of dict): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file

        Args:
            list_objs (list of Base instances): A list of
            instances to be saved

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            obj_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(obj_dicts)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string representing a
            list of dictionaries.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes already
        set using a dictionary

        Args:
            dictionary (dict): A dictionary containing
            attribute values

        Returns:
            Base: An instance with attributes set from the dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: A list of instances created from the file data.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                obj_dicts = cls.from_json_string(json_data)
                return [cls.create(**obj_dict) for obj_dict in obj_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of instances to a CSV file.

        Args:
            list_objs (list of Base instances): A list of
            instances to be saved.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    data = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file.

        Returns:
            list: A list of instances created from the file data.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = map(int, row)
                        instance = cls(width, height, x, y, id)
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, row)
                        instance = cls(size, x, y, id)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw rectangles and squares using Turtle graphics.

        Args:
            list_rectangles (list of Rectangle instances): A list
            of Rectangle objects
            list_squares (list of Square instances): A list of Square objects

        Returns:
            None
        """
        # Initialize the Turtle graphics screen
        turtle.Screen()
        turtle.title("Draw Rectangles and Squares")

        # Create a Turtle object for drawing
        pen = turtle.Turtle()
        pen.speed(1)  # Set the drawing speed (adjust as needed)

        # Draw rectangles
        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.color("blue")  # You can change the color
            pen.begin_fill()

            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)

            pen.end_fill()

        # Draw squares
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("green")  # You can change the color
            pen.begin_fill()

            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

            pen.end_fill()

        # Close the Turtle graphics window on click
        turtle.exitonclick()
