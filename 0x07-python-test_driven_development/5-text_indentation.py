#!/usr/bin/python3
"""defining a function that prints a text with 2 new lines
after each of these characters: ., ? and :
    Args:
        text: The text to print.
"""


def text_indentation(text):
    """this is the function that prints a text with 2 lines
    Raises:
        TypeError: If text is not a string"""
    if not isinstance(text, str):
        error_msg = "text must be a string"
        raise TypeError(error_msg)

    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
