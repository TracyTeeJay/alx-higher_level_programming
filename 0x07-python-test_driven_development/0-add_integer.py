#!/usr/bin/python3

"""
module containing addition function
"""


def add_integer(a, b=98):
    """
    function to add integers
    Arguments:
    a (int or float): first argument
    b (int or float): second argument
    return:
    int: sum of arguments
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
