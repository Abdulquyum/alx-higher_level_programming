#!/usr/bin/python3
""" returns an object (Python data structure) represented by a JSON string """

import json


def from_json_string(my_str):
    """ module that return python object representation of JSON """
    return json.loads(my_str)
