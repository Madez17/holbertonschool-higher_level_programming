#!/usr/bin/python3

"""Module matrix_divided
Documentation as specified by how can divided a matrix that receive how parameter, and receive other parameterthat is div it is the number by its goin to be divided the elements of the list of the matrix.

"""


def matrix_divided(matrix, div):

    """Example function matrix_divided.
    Args:
        matrix: First parameter.
        div: Second parameter.
    Return:
        return new matrix.
    """

    matrix_new = []
    for list in matrix:
        list_new = []
        for item_list in list:
            if type(item_list) is not int and type(item_list) is not float:
                raise TypeError('matrix must be a matrix (list of lists) \
 of integers/floats')
            if len(list) != len(matrix[0]):
                raise TypeError('Each row of the matrix must have the same size')
            if type(div) != int and type(div) != float:
                raise TypeError('div must be a number')
            if div == 0:
                raise ZeroDivisionError('division by zero')
            result = item_list / div
            list_new.append(round(result, 2))
        matrix_new.append(list_new)
    return matrix_new
