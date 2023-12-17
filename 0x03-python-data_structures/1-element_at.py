#!/usr/bin/python
def element_at(my_list, idx):
    if 0 <= idx < len(my_list):
        count = -1
        for x in my_list:
            count += 1
            if count == idx:
                return x
    else:
        return None
