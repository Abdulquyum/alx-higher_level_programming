#!/usr/bin/python3
'''
    Base of all other classes in the project
'''


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function to declare self """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
