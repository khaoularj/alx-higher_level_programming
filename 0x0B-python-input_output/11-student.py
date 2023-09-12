#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represent a student from the class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: first name of the student.
            last_name: last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """set a dictionary representation of the clss student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student

        Args:
            json: The dictionnary
        """
        for i, y in json.items():
            setattr(self, i, y)
