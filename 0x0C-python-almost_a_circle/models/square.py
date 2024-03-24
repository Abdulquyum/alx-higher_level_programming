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
