#!/usr/bin/python3
"""Module rectangle - object"""


class Rectangle(object):
    """Define Rectangle class"""
    def __init__(self, width=0, height=0):
        """
        Define 2 atributtes
        width
        height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """property to height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height value"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ area square side by side"""
        areaRectangle = self.__height * self.__width
        return areaRectangle

    def perimeter(self):
        """area perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        ph = self.__height * 2
        pw = self.__width * 2
        perimeter = ph + pw
        return perimeter

    def __str__(self):
        """Method str - return string"""
        if self.__width == 0 or self.__height == 0:
                return ''
        result = ''
        for x in range(self.height):
            if x < self.height - 1:
                result += self.width * '#' + '\n'
            else:
                result += self.width * '#'
        return result
