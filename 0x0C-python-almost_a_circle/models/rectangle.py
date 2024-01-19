#!/usr/bin/python3
"""
    class definition of a rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """ modules to define rectangle inheriting from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
<<<<<<< HEAD
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
=======
        ''' x setter func '''
>>>>>>> 1a49d0d51d35e9ee5b9c8488837191190bd8bc86
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' y getter mod '''
        return self.__y

    @y.setter
    def y(self, value):
<<<<<<< HEAD
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
=======
        ''' y setter mod '''
>>>>>>> 1a49d0d51d35e9ee5b9c8488837191190bd8bc86
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' returns the area of the rectangle '''
        return self.__height * self.__width

    def display(self):
        ''' Display rectangle with '#' representation
            considering x and y '''
        for a in range(self.__x):
            print()
        for b in range(self.__height):
            for c in range(self.__y):
                print(' ', end='')
            for d in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        ''' prints str representation '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

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
