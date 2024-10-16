#!/usr/bin/python3
"""Define a append_write function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): The name of the text file
        text (str): The text to append to the file

    Returns:
        int: The number of characters added to the file
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except FileNotFoundError:
        # If the file doesn't exist, create it and write the text
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
