#!/usr/bin/python3

"""
function that returns attributes of an object
"""


def lookup(obj):
    """
    returns all available attributes on object obj
    Args:
    obj (<class object>); python object
    """
    return dir(obj)
