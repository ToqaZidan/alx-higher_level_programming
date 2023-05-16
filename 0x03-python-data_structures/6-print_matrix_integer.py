#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for R in matrix:
        for C in R:
            print("{:d}".format(C), end=" " if C != R[-1] else "")
        print()
