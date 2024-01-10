#!/usr/bin/python3
""" write to file """


def write_file(filename="", text=""):
    """ open and write some texts to file """
    with open(filename, 'w', encoding="utf-8") as w:
        return w.write(text)
