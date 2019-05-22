#!/usr/bin/python3
class Square(object):
    def __init__(self, size=0):
        try:
            if type(size) != int:
                raise TypeError ('size must be an integer')
            else size < 0:
                raise ValueError ('size must be >= 0')
        finally:
            self.__size = size
        def area(self)
            return area.__self
