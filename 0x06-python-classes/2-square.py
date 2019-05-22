#!/usr/bin/python3
class Square(object):
    def __init__(self, size=0):
        try:
            if type(size) != int:
                raise TypeError('size must be a integer')
            elif size < 0:
                raise ValueError('size must be >= 0')
        finally:
            self.__size = size
