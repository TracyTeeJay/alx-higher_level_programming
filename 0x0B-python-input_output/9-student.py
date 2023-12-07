#!/usr/bin/python3

"""
contains class Student that defines a student

Attributes:
__init__(self, first_name, last_name, age): instantiates names and age
to_json(self): retreives dictionary representation of class
"""


class Student:
    """
    class Student with instance variables
    Attributes:
    __init__(self, first_name, last_name, age): instantiates names and age
    to_json(self): retreives dictionary representation of class
    """

    def __init__(self, first_name, last_name, age):
        """
        instantiation of variables
        Arguments:
        first_name (str): string with first name
        last_name (str): string with last name
        age (int): integer for age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns dictionary representation of the class Student
        """
        return self.__dict__
