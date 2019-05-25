#!/usr/bin/python3

"""Module print_square
This documentation is about how you can print a square where
you receive in size tha is the number that the function has validate
to print the number of times with the symbol #.

"""


def print_square(size):
    """Example function print square.

    Args:
        size: Unique parameter.

    Print:
        Print value. character * size.

    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    else:
        for x in range(size):
            print(size * '#')
