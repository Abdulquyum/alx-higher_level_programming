#!/usr/bin/python3

""" Area of Square """


class Square:
    """ Contains modules that define the square """
    def __init__(self, size=0):

        """ square muat be digit and
            must be greater than 0 """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
