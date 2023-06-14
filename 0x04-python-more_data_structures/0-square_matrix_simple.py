#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    row_column = []
    for i in matrix:
        row_column.append(list(map(lambda i: i**2, i)))
    return (row_column)
