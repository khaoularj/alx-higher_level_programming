#!/usr/bin/python3
"""define a function that returns the dictionary description"""


def class_to_json(obj):
    """fn that returns the dictionary description with simple data structure"""
    return obj.__dict__
