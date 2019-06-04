#!/usr/bin/python3
"""Module is kind of class"""


def is_kind_of_class(obj, a_class):
    """Module is same class
    Args: obj
    Print: a_class
    Return: True
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
