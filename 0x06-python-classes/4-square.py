#!/usr/bin/python3
class Square(object):
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.set_size(size)

    def get_size(self):
        return self.__size

    def set_size(self, value):
        self.__size = value
       
    def area(self):
        areaSquare = self.__size * self.__size
        return areaSquare
