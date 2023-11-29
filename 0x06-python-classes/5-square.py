#!/usr/bin/python3

"""
this is a module with a class named Square
"""


class Square:
    """
    this class represents Square and has the following:

    Attributes:
    __size (int): this is an integer representing the sides of Square
    """

    def __init__(self, size=0):
        """
        this function is called when class Square is initialized

        Args:
        size (int): used ti initialize the private attribute __size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        defines area of square represented in class

        Returns:
        int: area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter for the private instance __size
        Returns:
        int: length of side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for the private instance __size
        Args:
        value (int): sets size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        function to print square using #
        """
        if self.__size > 0:
            for cnt in range(self.__size):
                print("{}".format("#" * self.__size))
        else:
            print()
