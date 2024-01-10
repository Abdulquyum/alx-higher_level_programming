#!/usr/bin/python3
""" read file """


def read_file(filename=""):
    """ open and reads file and print content """
    with open(filename, 'r', encoding="utf-8") as q:
        read_file = q.read()
        if read_file is None:
            q.close()
    print(read_file, end="")
