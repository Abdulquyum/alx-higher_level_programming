#!/usr/bin/python3
def lookup(obj):
    """ look up for the list of available attributes
        and methods of an object """
    return list(dir(obj))
