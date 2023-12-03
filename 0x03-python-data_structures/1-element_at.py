#!/usr/bin/python
def element_at(my_list, idx):
    i = len(my_list) - 1
    if idx < 0:
        return none
    elif idx > i:
        return 0
    else:
        return my_list[idx]
