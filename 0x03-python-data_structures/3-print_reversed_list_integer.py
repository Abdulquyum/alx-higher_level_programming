#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    else:
        x = len(my_list) - 1
        result = []
        while x >= 0:
            result.append(my_list[x])
            x -= 1
        for i in result:
            print("{:d}".format(i))
