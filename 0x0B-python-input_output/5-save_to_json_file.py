#!/usr/bin/python3
"""function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """this function writes an Object to a text file using JSON rep"""
    with open(filename, "w") as n_file:
        json.dump(my_obj, n_file)
