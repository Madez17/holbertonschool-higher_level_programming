#!/usr/bin/python3
class Square(object):
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        areaSquare = self.__size * self.__size
        return areaSquare

    def my_print(self):
        if self.__size != 0:
            for x in range(self.__size):
                print('#' * self.__size)
        else:
            print()
