#!/usr/bin/python3
def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    and returns the number of characters written
    Args:
        filename: name of the file
        text: the text to write
    Returns:
        the number of characters written"""
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
