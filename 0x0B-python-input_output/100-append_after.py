#!/usr/bin/python3
"""define a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file
    after each line containing a specific string
    Args:
        filename: name of the file
        search_string: string to search for
        new_string: string to insert"""

    fl_text = ""
    with open(filename) as i:
        for k in i:
            fl_text += k
            if search_string in k:
                fl_text += new_string
    with open(filename, "w") as w:
        w.write(fl_text)
