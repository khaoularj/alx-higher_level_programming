#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(args[0], args[1])
        return res
    except Exception:
        error_m = "Exception: {}".format((sys.exc_info()[1]), file=sys.stderr)
        print(error_m)
        return None
