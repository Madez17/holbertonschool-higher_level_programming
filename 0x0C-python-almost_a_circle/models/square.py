#!/usr/bin/python3
"""Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class construct object """
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """Method str show objects"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)
