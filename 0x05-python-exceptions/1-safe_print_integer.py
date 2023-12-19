#!/bin/usr/python3
def safe_print_integer(value):
    try:
        for i in value:
            if i.isdigit() is True:
                print("{:d}".format(i))
        return True
    except:
        return False
