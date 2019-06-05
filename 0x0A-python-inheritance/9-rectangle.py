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
        """Module
        Args: self
        Args: name
        Args: value
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle """
    def __init__(self, width, height):
        """ Module int
        Args: Self
        Args: width
        Args: height
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)
        print("[Rectangle] {}/{}".format(width, height))

    def area(self):
        """Module area
        Args: Self
        """
        return self.__width * self.__height
