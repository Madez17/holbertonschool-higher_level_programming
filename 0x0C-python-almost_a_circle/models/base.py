#!/usr/bin/python3
""" Base Module"""


class Base(object):
    """Class definition - Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class - onstructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
