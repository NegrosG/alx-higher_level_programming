#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        square_matrix.append([j**2 for j in i])
    return square_matrix
