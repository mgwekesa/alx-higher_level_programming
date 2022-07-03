#!/usr/bin/python3

""" the function divides the elements of a matrix with a div"""


def matrix_divided(matrix, div):
    """
    takes matrix and div as mandatory parameters

    Return:
        a new matrix formed by diving matrix by div
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(err_msg)
    if not isinstance(matrix, list):
        raise TypeError(err_msg)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(err_msg)
        for item in lists:
            if type(item) not in [int, float]:
                raise TypeError(err_msg)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(err_msg)
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
