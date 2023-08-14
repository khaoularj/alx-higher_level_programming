#!/usr/bin/python3
def no_c(my_string):
    n_string = [x for x in my_string if x != 'c' and x!= 'C']
    #my_string.replace(c_to_rm, '').replace(C_to_rm, '')
    return ("".join(n_string))
