#!/usr/bin/python3
""" inherits from list and prints sorted list """


class MyList(list):
    """ contain module to sort list
        in ascending order """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
