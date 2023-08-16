#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def sqr(x):
        return (x ** 2)
    res_matrix = []
    for row in matrix:
        sqr_row = list(map(sqr, row))
        res_matrix.append(sqr_row)
    return res_matrix
