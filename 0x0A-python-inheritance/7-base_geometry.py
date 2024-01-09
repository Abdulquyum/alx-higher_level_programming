#!/usr/bin/python3
""" define BaseGeometry class """


class BaseGeometry(object):
    """ A defined method of BaseGeometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError(self.name + ' ' + "must be an integer")
        elif value < 0:
            raise (self.name + ' ' + "must be greater than 0")
