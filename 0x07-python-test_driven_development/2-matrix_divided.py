#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    for row in matrix:
        for col in matrix:
            #if not isinstance(col, int) or not isinstance(col, float):
                #raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            #elif len(row) != len(col):
                #raise TypeError("Each row of the matrix must have the same size")
            #elif not isinstance(div, int) or not isinstance(div, float):
                #raise TypeError("div must be a number")
            #elif div == 0:
                #raise ZeroDivisionError("division by zero")
            new_matrix.append(col / div)
    return new_matrix
