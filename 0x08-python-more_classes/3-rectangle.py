#!/usr/bin/python3

""" defines a real Rectangle """


class Rectangle:
    """ A rectangle with width and height
        also with calculated perimeter and area """
    def __init__(self, width=0, height=0):
        """ rectangle height and width value must be an integer
            and its height and width must be greater then 0 """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width != 0 or self.__height != 0:
            for a in range(self.__height):
                for i in range(self.__width):
                    print("#", end="")
                if a != self.__height - 1:
                    print()
        return " "
