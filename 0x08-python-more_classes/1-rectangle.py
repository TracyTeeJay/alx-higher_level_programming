#!/usr/bin/python3

"""
function to define a class: Rectangle
"""


class Rectangle():
    """
    represents class Rectangle with:
    Attributes:
    width (int):
    height (int):
    """

    def __init__(self, width=0, height=0):
        """
        initializes the private atrributes when class Rectangle is called

        Attributes:
        width (int): short side of rectangle
        height (int): longer side of rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        gives access to private attribute width
        """
        return self.__width

    @property
    def height(self):
        """
        gives access to private attribute height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        sets value fir width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
        sets value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
