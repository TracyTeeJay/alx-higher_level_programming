#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    mtrx_sq = []

    for ints in matrix:
        squares = list(map(lambda x: x ** 2, ints))

        mtrx_sq.append(squares)
    return mtrx_sq
