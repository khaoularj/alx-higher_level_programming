#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        format_value = "{:d}".format(value)
        print(format_value)
        return True
    except Exception:
        error_m = "Exception: {}".format((sys.exc_info()[1]))
        print(error_m, file=sys.stderr)
        return False
