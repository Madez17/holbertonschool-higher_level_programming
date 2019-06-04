#!/usr/bin/python3
"""Module Nothing"""


class MyList(list):
    """Class MyList """

    def print_sorted(self):
        """Module lookup object
        Args: self
        Print: sort_cpy
        """
        sort_cpy = self[:]
        sort_cpy.sort()
        print(sort_cpy)
