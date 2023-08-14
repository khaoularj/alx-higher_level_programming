#!/usr/bin/python3
def no_c(my_string):
    c_to_rm = 'c'
    C_to_rm = 'C'
    n_string = my_string.replace(c_to_rm, '').replace(C_to_rm, '')
    print(n_string)
