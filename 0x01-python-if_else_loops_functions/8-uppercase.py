#!/usr/bin/python3
# the function that prints a string in uppercase followed by a new line

def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
