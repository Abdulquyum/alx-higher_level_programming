#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        while idx < x:
            print("{:d}".format(my_list[idx]), end='')
            idx += 1
        return x
    except Exception:
        count = 0
        for x in my_list:
            count += 1
        return count
