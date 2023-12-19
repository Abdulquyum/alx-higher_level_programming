#!/bin/usr/python3
def raise_exception_msg(message=""):
    try:
        raise NameError
    except NameError:
        ("{:s}".format(message))
