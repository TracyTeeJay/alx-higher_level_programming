#!/usr/bin/python3

"""
function that gives JSON representation
"""
import json


def to_json_string(my_obj):
    """
    returns object converted to JSON string
    Args:
    my_obj (str): object to be serialized
    """
    strObj = json.dumps(my_obj)

    return strObj
