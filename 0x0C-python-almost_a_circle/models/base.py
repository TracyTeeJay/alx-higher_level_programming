#!/usr/bin/python3

"""
contains class called Base
"""


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
