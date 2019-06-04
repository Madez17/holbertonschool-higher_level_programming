#!/usr/bin/python3
"""Module is a same class"""


def is_same_class(obj, a_class):
    """Module is same class
    Args: obj
    Print: a_class

    Return: True
    """
    if type(obj) == a_class:
        return True
    else:
        return False
