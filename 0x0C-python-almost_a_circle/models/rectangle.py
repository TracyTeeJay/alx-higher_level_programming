#!/usr/bin/python3

"""
contains calss Rectangle that inherits from Base
"""

from models.base import Base

class Rectangle(Base):
    """
    contains the following:
    Attributes:
    __init__(self, width, height, x=0, y=0, id=None):
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instantiates the attributes of Rectangle
        Args:
        width (int):
        height (int):
        x (int):
        y (int):
        id (int): integer assigned to self.id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width value """
        if type(value) is not int:
            Rectangle.raiseNotIntegerError("width")
        if value <= 0:
            Rectangle.raiseValueLessThanOrEqualToZeroError("width")        
        self.__width = value

    @property
    def height(self):
        """ get height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height value """
        if type(value) is not int:
            Rectangle.raiseNotIntegerError("height")
        if value <= 0:
            Rectangle.raiseValueLessThanZeroError("height")
        self.__height = value

    @property
    def x(self):
        """ get x value """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x value """
        if type(value) is not int:
            Rectangle.raiseNotIntegerError("x")
        if value < 0:
            Rectangle.raiseValueLessThanZeroError("x")
        self.__x = value


    @property
    def y(self):
        """ get y value """
        return self.__y
    
    @y.setter
    def y(self, value):
        """ sets y value """
        if type(value) is not int:
            Rectangle.raiseNotIntegerError("y")
        if value < 0:
            Rectangle.raiseValueLessThanOrEqualToZeroError
        self.__y = value
