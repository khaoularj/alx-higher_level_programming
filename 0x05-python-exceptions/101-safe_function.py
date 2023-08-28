#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception:
        error_m = "Exception: {}".format(sys.exc_info()[1])
        print(error_m, file=sys.stderr)
        return None
