#!/usr/bin/python3

""" class defines a square """


class Square:
    """contains a module with definition """

    def __init__(self, size=0):
        """inside module checking if size is of int type
            or if size is less than 0 """
        self.__size = size
        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
        except Exception:
            if size < 0:
                raise ValueError("size must be >= 0")
