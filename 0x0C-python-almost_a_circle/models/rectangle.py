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
            Rectangle.raiseValueLessThanZeroError
        self.__y = value

    @staticmethod
    def raiseNotIntegerError(propName):
        """
        raise a TypeError when a non integer is input
        """
        raise TypeError("{} must be an integer".format(propName))

    @staticmethod
    def raiseValueLessThanOrEqualToZeroError(propName):
        """
        raise a ValueError when a negative or zero is input
        """
        raise ValueError("{} must be > 0".format(propName))

    @staticmethod
    def raiseValueLessThanZeroError(propName):
        """
        raises a ValueError when a negative number is input
        """
        raise ValueError("{} must be >= 0".format(propName))

    def area(self):
        """
        calculates area of rectangle
        Args:
        height (int):
        width (int):
        """
        return (self.__width * self.__height)

    def display(self):
        """
        prints out the instance Rectangle with the character '#'
        """
        for cnt in range(self.__y):
            print()

        lineR = "#" * self.__width
        spaceR = " " * self.__x
        for cnt in range(self.__height):
            print(spaceR + lineR)

    def __str__(self):
        """
        return a string representation of the instance Rectangle
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        function to update attributes ofRectangle in order
        """
        for key, value in enumerate(args):
            if key == 0:
                self.id = value
            elif key == 1:
                self.width = value
            elif key == 2:
                self.height = value
            elif key == 3:
                self.x = value
            elif key == 4:
                self.y = value

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.width = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y == value

    def to_dictionary(self):
        """
        Return a dictionary representation of rectangle instance
        """
        rectangle_dict = {}
        rectangle_dict["id"] = self.id
        rectangle_dict["width"] = self.width
        rectangle_dict["height"] = self.height
        rectangle_dict["x"] = self.x
        rectangle_dict["y"] = self.y
        return rectangle_dict
