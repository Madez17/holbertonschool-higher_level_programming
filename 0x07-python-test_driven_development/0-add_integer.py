#!/usr/bin/python3

"""Module add_integer
Documentation as specified by how can add two numbers
and the diferents conditions when you pass paramethers and this validate when
have a error.

"""


def add_integer(a, b=98):

    """Example function add integer.
    Args:
        a: First parameter.
        b: Second parameter.
    Return:
        return value. a + b.
    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
