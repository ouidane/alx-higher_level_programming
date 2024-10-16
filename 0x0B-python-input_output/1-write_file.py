#!/usr/bin/python3
"""Define a write_file function"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename (str): The name of the text file
        text (str): The text to write to the file

    Returns:
        int: The number of characters written to the file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except FileNotFoundError:
        # If the file doesn't exist, create it and write the text
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
