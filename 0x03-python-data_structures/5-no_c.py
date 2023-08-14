#!/usr/bin/python3
def no_c(my_string):
    c_to_rm = 'c'
    C_to_rm = 'C'
    n_string = [x for x in my_string if x != c_to_rm and x!= C_to_rm]
    #my_string.replace(c_to_rm, '').replace(C_to_rm, '')
    return ("".join(n_string))
