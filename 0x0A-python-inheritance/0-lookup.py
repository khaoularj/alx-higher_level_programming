#!/usr/bin/python3
"""define the object lookup"""


def lookup(obj):
    """this function return a list of an object's available attributes"""
    r = dir(obj)
    return r
