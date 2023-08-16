#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = list(a_dictionary.keys())
    new_list.sort()
    for items in new_list:
        value_key = a_dictionary.get(items)
        print("{}: {}".format(items, value_key))
