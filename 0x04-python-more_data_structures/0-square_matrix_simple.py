#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = list(map(list, matrix))
    new_matrix = [[y**2 for y in x] for x in new_matrix]
    return new_matrix
