#!/usr/bin/python3
""" writing an Object to a text file, using a JSON representation """


import json


def save_to_json_file(my_obj, filename):
    ''' A module implementing writing an object to a textfile
        using JSON '''
    with open(filename, 'w', encoding="utf-8") as s:
        s.write(json.dumps(my_obj))
