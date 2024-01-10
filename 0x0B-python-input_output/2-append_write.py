#!/usr/bin/python3
""" append to file """


def append_write(filename="", text=""):
    """ open and append texts to file """
    with open(filename, 'a', encoding="utf-8") as app:
        return app.write(text)
