#!/usr/bin/python3
""" define function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
    Args:
        filename: name of the file
        text: text to append
    Returns: the number of characters added"""
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
