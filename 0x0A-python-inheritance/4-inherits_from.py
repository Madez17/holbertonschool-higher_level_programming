#!/usr/bin/python3
"""Module inherits """


def inherits_from(obj, a_class):
    """Module is same class
    Args: obj
    Print: a_class
    Return: True
    """
    if type(obj) == a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
