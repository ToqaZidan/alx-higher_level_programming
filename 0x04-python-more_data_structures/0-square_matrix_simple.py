#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    A function that computes the square value of all
    integers of a matrix.
    '''
    NewList = []
    if len(matrix) == 0:
        return NewList

    NewList = [[i*i for i in j] for j in matrix]
    return NewList
