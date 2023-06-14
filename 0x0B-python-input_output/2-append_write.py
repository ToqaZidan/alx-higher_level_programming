#!/usr/bin/python3
"""A module to Define a file-appending function."""


def append_write(filename="", text=""):
    """
    A function to Appends a string
    to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as new_file:
        return new_file.write(text)
