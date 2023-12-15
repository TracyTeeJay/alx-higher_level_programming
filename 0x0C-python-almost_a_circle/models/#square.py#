#!/usr/bin/python3

"""
contains a class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    function to display a square
    Arguments:
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        instantiates the instance Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get the value of size """
        return self.width

    @size.setter
    def size(self, value):
        """ set the value for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ return a string representation of this instance """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
