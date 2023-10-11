#!/usr/bin/python3
"""define function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)
    Args:
        my_obj: the string to be serialized
    Returns: the JSON representation of the string"""
    return json.dumps(my_obj)
