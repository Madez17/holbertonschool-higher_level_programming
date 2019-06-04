#!/usr/bin/python3
"""Module base geometry"""


class BaseGeometry(object):
    """ clase BaseGeometry"""
    def area(self):
        """ Module area
        Args: self
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
