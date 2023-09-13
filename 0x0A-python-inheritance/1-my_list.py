#!/usr/bin/python3
"""define a class MyList that inherits from list"""


class MyList(list):
    """this is the class MyList"""

    def print_sorted(self):
        """it prints the list, but sorted (ascending sort)"""
        print(sorted(self))
