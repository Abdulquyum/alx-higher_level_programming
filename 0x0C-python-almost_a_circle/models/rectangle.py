#!/usr/bin/python3
"""
    class definition of a rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """ modules to define rectangle inheriting from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be integer".format(self.__width))
        if value <= 0:
            raise ValueError("{} must be > 0".format(self.__width))
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.__height))
        if value <= 0:
            raise ValueError("{} must be > 0".format(self.__height))
        self.__height = value

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("{} must be >= 0".format(self.__x))
        self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("{} must be >= 0".format(self.__y))
        self.__y = value
