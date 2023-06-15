#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda row_column: [x ** 2 for x in row_column], matrix))
