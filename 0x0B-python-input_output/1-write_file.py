#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """Write a string to a text file UTF8.

    Args:
        filename : name of the file to write.
        text : text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as n_file:
        return n_file.write(text)
