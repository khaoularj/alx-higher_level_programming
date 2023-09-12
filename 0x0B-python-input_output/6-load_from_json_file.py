#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename) as n_file:
        return json.load(n_file)
