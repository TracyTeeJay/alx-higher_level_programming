#!/usr/bin/python3

"""
function to deserialize json to string
"""

import json


def from_json_string(my_str):
    """
    deserializes a json string
    Args:
    my_str (json string): the string to be deserialized
    """
    strObj = json.loads(my_str)

    return strObj
