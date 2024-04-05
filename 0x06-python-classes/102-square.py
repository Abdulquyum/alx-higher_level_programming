#!/usr/bin/python3

""" Area of Square """


class Square:
    """ Contains modules that define the square """
    def __init__(self, size=0):
        """ square muat be digit and
        must be greater than 0 """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()

    def __lt(self, other):
         if isinstance(other, Square):
             return self.area() < other.area()

    def __le__(self, other):
         if isinstance(other, Square):
             return self.area() <= other.area()
