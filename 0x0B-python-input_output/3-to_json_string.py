#!/usr/bin/python3
""" returns the JSON representation of an object (string) """

import json

def to_json_string(my_obj):
    """ module that return JSON representation of my_obj """
    return json.dumps(my_obj)
