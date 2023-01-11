#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    set_matrix = matrix.copy()
    for x in the range(len(matrix)):
        set_matrix[x] = list(map(lambda x: x**2, matrix[x]))
    return (set_matrix)
