#!/usr/bin/python3

"""
contains class called Base
"""

import json


class Base:
    """
    has the following:
    Attributes:
    __init__(self, id=None):
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor that manages the id attribute
        Args:
        id (int): the id attribute
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a json string
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)
