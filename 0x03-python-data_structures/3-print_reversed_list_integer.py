#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list) - 1
    while x <= 0:
        my_list.append(my_list[x])
        print("{}".format(my_list))
        x -= 1
