#!/usr/bin/python3
"""define a new class student"""


class Student:
    """this class define a student"""
    def __init__(self, first_name, last_name, age):
        """this is the constructor
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            res = {}
            for y in attrs:
                if hasattr(self, y):
                    res[y] = getattr(self, y)
            return res
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
