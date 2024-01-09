#!/usr/bin/python3
def def is_kind_of_class(obj, a_class):
    """ check if the object is an instance of, or
        if the object is an instance of a class that inherited from """
    if isinstance(obj, a_class):
        return True
    else:
        return False
