#!/usr/bin/python3

"""

this is a definitinion of class: Square

"""


class Square:
    """

    this represents the  class Square and has the following:

    Attributes:
    __size(int): this is an integer representing the size of a side of square

    """

    def __init__(self, size=0):

        """
        function that initializes when class is called. It has the following:

        Args:
        size (int): this initializes the private attribute __size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates the area of the square the class represent

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        A getter for the __size private instance attribute

        Returns:
            int: the length of a side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A setter for the __size private instance attribute

        Args:
            value (int): used to set the size of the Square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
