#!/usr/bin/python3

"""
contains a function that creates an object from a json file
"""

import json


def load_from_json_file(filename):
    """
    returns python object
    Args:
    filename (str): name of file or path to it
    """
    with open(filename, "r") as file:
        obj = json.load(file)
        return obj
