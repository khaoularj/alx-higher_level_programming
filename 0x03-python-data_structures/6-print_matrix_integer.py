#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        r_str = " ".join(["{:d}".format(n) for n in row])
        print(r_str)
