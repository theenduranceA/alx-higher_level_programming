#!/usr/bin/python3
"""Module of division."""


def matrix_divided(matrix, div):
    """Function that divides all the elements of a matrix"""

    Message = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != list:
        raise TypeError(Message)
    if any(type(x) != list for x in matrix):
        raise TypeError(Message)
    if len(matrix) == 0:
        raise TypeError(Message)
    size = len(matrix[0])
    for x in matrix:
        if len(x) != size:
            raise TypeError("Each row of the matrix must have the same size")
        if len(x) == 0:
            raise TypeError(Message)
        for y in x:
            if type(y) != int and type(y) != float:
                raise TypeError(Message)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return(
        list(map(lambda v: list(map(lambda n: round(n / div, 2), v)), matrix))
    )
