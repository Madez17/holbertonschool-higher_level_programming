#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for num in matrix:
        mtrx = []
        for column in num:
            mtrx.append(column * column)
        new_matrix.append(mtrx)
    return new_matrix
