#!/usr/bin/python3
""" check if the object is a subclass """


def inherits_from(obj, a_class):
    """  if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class """
    if issubclass(type(obj), a_class):
        return True
    else:
        False
