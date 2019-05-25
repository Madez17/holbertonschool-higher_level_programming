#!/usr/bin/python3

"""
Module say_my_name
Documentation as specified how can print a string and this function
receive two parameters and before that this verify if this paramethers
there aren't a string, but if is a string this print.

"""


def say_my_name(first_name, last_name=""):
    """Example function print string.

    Args:
        First_name: First parameter.
        last_name: Second parameter.

    Print:
        Print value string.

    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
