#!/usr/bin/python3
'''  returns the list of available attributes and methods of an object '''


def lookup(obj):
    """ look up for the list of available attributes
        and methods of an object """

    return list(dir(obj))
