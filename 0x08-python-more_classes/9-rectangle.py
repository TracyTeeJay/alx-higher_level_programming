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
    number_of_instances = 0
    print_symbol = '#'

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

        Rectangle.number_of_instances += 1

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
        sets value for width
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

    def area(self):
        """
        function to calculate area of rectangle
        returns:
        int: product of width and height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        function to calculate the preimeter of rectangle
        returns:
        int: sum of twice height and twice width
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Prints Rectangle using # or any other given character

        Returns:
        str: formatted string
        """
        # frmtStr = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        hashStr = str(self.print_symbol)
        hashList = []
        for cnt in range(self.__height):
            for cnt1 in range(self.__width):
                hashList.append(hashStr)
            # frmtStr += f"{hashStr * self.__width}"
            if cnt + 1 != self.__height:
                hashList.append("\n")

        return "".join(hashList)

    def __repr__(self):
        """
        Print expression for instantiating another Rectangle

        Returns:
        str: formatted string
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        notifies when objec is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        function to compare two rectangles
        Args:
            rect_1 (Rectangle): an instance of Rectangle
            rect_2 (Rectangle): an instance of Rectangle
        Returns:
            <class Rectangle>
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2

        return rect_1

    @classmethod
    def square(cls, size=0):
        """
        function that prints a square as arectangle
        Args:
        size (int): side of square
        returns:
        instance of rectangle
        """
        return cls(size, size)

    def __repr__(self):
        """
        Returns a string representation of the class

        """

        return f"Rectangle({self.__width}, {self.__height})"
