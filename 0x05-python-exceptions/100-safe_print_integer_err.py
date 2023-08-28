#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        format_value = "{:d}".format(value)
        print(format_value)
        return True
    except(ValueError, TypeError):
        error_m = "Exception: {}".format((sys.exc_info()[1]), file=sys.stderr)
        print(error_msg)
    return False
