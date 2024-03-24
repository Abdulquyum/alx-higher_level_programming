#!/usr/bin/python3
""" Sqaure definition """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ consists of Module that amkes square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization of inherited factors """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ prints string representation """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        ''' width getter function '''
        return self.__width

    @size.setter
    def size(self, value):
        ''' width getter function '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    @property
    def x(self):
        ''' x getter func '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' x setter func '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' y getter mod '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' y setter mod '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
