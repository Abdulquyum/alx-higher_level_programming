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
    def width(self):
        ''' width getter function '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width getter function '''
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' height getter module '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter module '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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

    def update(self, *args, **kwargs):
        """ updates rectangle with the aid of
        args and kwargs """
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception as s:
                pass
            else:
                self.id = kwargs.get('id', self.id)
                self.width = kwargs.get('width', self.__width)
                self.height = kwargs.get('height', self.__height)
                self.x = kwargs.get('x', self.__x)
                self.y = kwargs.get('y', self.__y)
