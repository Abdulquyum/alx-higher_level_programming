#!/usr/bin/python3
def read_file(filename=""):
    """ open and reads file and print content """
    with open(filename, 'r', encoding="utf-8") as q:
        read_file = q.read()
    print(read_file)
