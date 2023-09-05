#!/usr/bin/python3
"""defining that divides all elements of a matrix.
    Args:
        matrix : A list of lists of ints or floats.
        div : divided number
"""


def matrix_divided(matrix, div):
    """ Raises:
            TypeError: If the lists contains non-numbers.
            TypeError: If thesizesof rows are different.
            TypeError: If div is not an int or float"""
    type_error_m = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(type_error_m)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        type_error = "Each row of the matrix must have the same size"
        raise TypeError(type_error)

    if not isinstance(div, (int, float)):
        error_division = "div must be a number"
        raise TypeError(error_division)

    if div == 0:
        error_div_zero = "division by zero"
        raise ZeroDivisionError(error_div_zero)

    div_result = []

    for row in matrix:
        n_row = [round(i / div, 2) for i in row]
        div_result.append(n_row)

    return div_result
