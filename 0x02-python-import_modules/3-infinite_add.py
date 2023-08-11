#!/usr/bin/python3
import sys
args = sys.argv[1:]
res = 0
for i in args:
    res = res + int(i)
print("{}".format(res))
