#!/usr/bin/python3

"""

this is a class named: Square

"""


class Square:
    """
    this represents the calss: Square with the following:

    Atributes:
    __size(int): representing the size of a side of square
    """

    def __init__(self, size=0):
        """
        this function is called when calss Square is initialized.

        Args:
        size (int): is used to initialize the private attribute __size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        this function calculates the area of the square represented in Square

        returns:
        int: area of square
        """

        return self.__size ** 2
