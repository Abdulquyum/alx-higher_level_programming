#!/usr/bin/python3
def uppercase(string):
    for q in string:
        if ord(q) >= 97 and ord(q) <= 122:
            q += 32
    print("{}".format(string))
