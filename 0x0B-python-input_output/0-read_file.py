#!/usr/bin/python3

"""
function to read a file
"""


def read_file(filename=""):
    """
    returns
    Args:
    filename (str): path to file
    """
    with open(filename, "r", encoding="utf-8") as file:
        cntnt = file.read()
        print(cntnt, end="")
