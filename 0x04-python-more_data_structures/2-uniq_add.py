#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = set(my_list)
    sum_list = 0
    for i in set_list:
        sum_list += i
        set_list.add(i)
    return sum_list
