#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return (None)
    n_max = my_list[0]
    for x in my_list:
        if x > n_max:
            n_max = x
    return n_max
