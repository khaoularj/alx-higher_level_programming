#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for n in my_list:
        mult_res = (n % 2)
        if mult_res == 0:
            res.append(True)
        else:
            res.append(False)
    return res
