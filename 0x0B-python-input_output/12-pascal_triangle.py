#!/usr/bin/python3

"""
contains function def pascal_triangle(n):
"""


def pascal_triangle(n):
    """
    function to calculate the pascal triangle
    Args:
    n (int): triangle  number
    """
    matrixx = []
    for cnt in range(1, n + 1):
        row = prevRow = []
        if cnt > 1:
            prevRow = matrixx[cnt - 2]
        for cnt2 in range(cnt):
            if cnt2 == 0 or cnt2 + 1 == cnt:
                row.append(1)
            else:
                row.append(prevRow[cnt2] + prevRow[cnt2 - 1])
        matrixx.append(row)
    return(matrixx)
