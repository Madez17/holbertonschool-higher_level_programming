#!/usr/bin/python3
"""Base """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle instance Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """ Method str show objects """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def display(self):
        """Class constructor actualization reactangle"""
        print(self.y * '\n', end='')
        for iter1 in range(self.__height):
            print(self.x * ' ', end='')
            print(self.__width * '#')

    def area(self):
        """ Class constructor area"""
        return self.width * self.height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter value width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('widt must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter value height """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter value x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter value y"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value
