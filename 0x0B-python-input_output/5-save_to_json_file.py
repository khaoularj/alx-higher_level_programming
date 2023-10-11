#!/usr/bin/python3
"""define function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON repr
    Args:
        my_obj: the object
        filename:the name of the file"""
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
