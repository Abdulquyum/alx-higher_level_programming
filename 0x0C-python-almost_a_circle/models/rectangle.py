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
