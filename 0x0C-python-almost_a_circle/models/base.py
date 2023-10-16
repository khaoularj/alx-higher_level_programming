#!/usr/bin/python3
"""Define a class called Base"""
import json


class Base:
    """this is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is a new constructor
        Args:
            @id: id of the new constructor(base)"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """adding the static method that returns the
        JSON string representation of list_dictionaries
        Args:
            list_dictionaries: is a list of dictionaries
        Return: the JSON serialization of a list_dictionaries"""
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        encod_json = json.dumps(list_dictionaries)
        return encod_json

    @classmethod
    def save_to_file(cls, list_objs):
        """adding the class method that writes the
        JSON string representation of list_objs to a file
        Args:
            list_objs: is a list of instances who inherits of Base"""
        """if list_objs is None:
            list_objs = []"""
        f_name = cls.__name__ + ".json"
        with open(f_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
        """dicts_obj = []
        for objects in list_objs:"""
            else:
                dicts_obj = [objects.to_dictionary()) for objects in list_objs]
                json_fl = json.dumps(dicts_obj)

        """with open(f_name, "w") as json_file:
            json_file.write(json_fl)"""

    @staticmethod
    def from_json_string(json_string):
        """adding the static method that returns
        the list of the JSON string representation json_string
        Args:
            json_string: is a string representing a list of dictionaries
        Return: the JSON deserialization of a list_dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
