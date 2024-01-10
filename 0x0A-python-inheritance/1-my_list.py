#!/usr/bin/python3
""" inherits from list and prints sorted list """


class MyList(list):
    """ contain module to sort list
        in ascending order """
    new_list = []
    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
