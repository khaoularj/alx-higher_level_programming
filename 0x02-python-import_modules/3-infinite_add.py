#!/usr/bin/python3
import sys
if __name__ == "__main__":
    rang = sys.argv[1:]
    res = 0
    for i in rang:
        res = res + int(i)
    print("{}".format(res))
