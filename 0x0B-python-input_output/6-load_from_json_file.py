#!/usr/bin/python3
"""define a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename) as fl:
        return json.load(fl)
