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

    def update(self, *args, **kwargs):
        """
        function to update attributes of Square in order
        """
        for key, value in enumerate(args):
            if key == 0:
                self.id = value
            elif key == 1:
                self.size = value
            elif key == 2:
                self.x = value
            elif key == 3:
                self.y = value

        if len(args):
            return

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.size = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
