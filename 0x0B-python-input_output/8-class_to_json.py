#!/usr/bin/python3

"""
function that returns dictionary description for JSON serialized object
"""

import json


def class_to_json(obj):
    """
    returns description of simple data structure
    Args:
    obj (list | dict | str | int | bool):where dictionary description is
    """
    return obj.__dict__
