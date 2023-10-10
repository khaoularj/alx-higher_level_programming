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

    def to_json(self):
        return self.__dict__
