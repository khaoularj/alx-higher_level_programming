#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """this function appends a string at the end of a text file
    and returns the number of characters added

    Args:
        filename : name of the file to append to.
        text : The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as n_file:
        return n_file.write(text)
