#!/usr/bin/python3
""" Base Module"""
import json


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

        newList = []

        with open(file_saved_obj, mode='w', encoding='UTF8') as MyFile:
           
            if list_objs is None:
                pass

            else:
                for obj in list_objs:
                    newList.append(obj.to_dictionary())
            MyFile.write(Base.to_json_string(newList))
