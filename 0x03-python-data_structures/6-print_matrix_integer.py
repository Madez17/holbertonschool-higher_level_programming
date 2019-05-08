#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            if (k != len(matrix)-1):
                print(matrix[j][k], end=' ')
            else:
                print(matrix[j][k], end='')
        print()
