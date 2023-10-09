#!/usr/bin/python3
"""Define a class MyList that inherits from list"""


class MyList(list):
    """define a public instance method"""
    def print_sorted(self):
        """this method prints the list, but sorted (ascending sort)"""
        print(sorted(self))
