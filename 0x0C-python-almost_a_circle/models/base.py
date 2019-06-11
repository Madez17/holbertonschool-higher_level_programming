#!/usr/bin/python3
import json
""" Base Module"""


class Base(object):
    """Class definition - Base"""
    __nb_objects = 0

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def __init__(self, id=None):
        """Class - onstructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
