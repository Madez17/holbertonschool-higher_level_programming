#!/usr/bin/python3
import json
""" Base Module"""


class Base(object):
    """Class definition - Base"""
    __nb_objects = 0

    """def from_json_string(json_string):"""

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method to convert a list to string """
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method save objects in new file"""
        file_saved_obj = cls.__name__ + '.json'

        """if list_objs is None:
            with open(file_saved_obj, mode='w', encoding='UTF8') as MyFile
                MyFile.write(json.dumps())"""
        newList = []
        for obj in list_objs:
            newList.append(obj.to_dictionary())

        with open(file_saved_obj, mode='w', encoding='UTF8') as MyFile:
            MyFile.write(Base.to_json_string(newList))

    def __init__(self, id=None):
        """Class - onstructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
