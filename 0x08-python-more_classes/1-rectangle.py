#!/usr/bin/python3

"""Module Reactangle - object"""


class Rectangle(object):
    """Rectangle class defined"""
    def __init__(self, width=0, height=0):
        """Definition atributtes class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """decorator property to width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter value"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Decorator property to height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Decorator setter height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
