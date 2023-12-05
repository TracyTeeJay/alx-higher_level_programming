#!/usr/bin/python3

"""
contains function inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a class that inherited
    """
    for cls in type(obj).__mro__:
        if cls is not a_class and issubclass(cls, a_class):
            return True

    return False
