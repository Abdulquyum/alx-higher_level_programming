#!/usr/bin/python3
""" Prints square """


def print_square(size):
    ''' Module to print square with '#' representation '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for a in range(size):
        for b in range(size):
            print("#", end="")
        print()
