#!/usr/bin/python3

"""
function that writes object to text form using json format
"""

import json


def save_to_json_file(my_obj, filename):
    """
    returns test string
    Args:
    my_obj (object): object to be serialized
    filename (str): name of file or path to be stored in
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
