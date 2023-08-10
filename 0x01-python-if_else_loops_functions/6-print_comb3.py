#!/usr/bin/python3
for n_1 in range(0, 10):
    for n_2 in range(n_1 + 1, 10):
        if n_1 == 8 and n_2 == 9:
            print("{}{}".format(n_1, n_2))
        elif n_1 != n_2:
            print("{}{}".format(n_1, n_2), end=", ")
