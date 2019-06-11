#!/usr/bin/python3
"""Base module square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class costruct square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class construct object """

        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """constructor To dictionary """
        nw_dictionary = {}
        nw_dictionary = Rectangle.to_dictionary(self)
        nw_dictionary['size'] = nw_dictionary['width']
        del nw_dictionary['width']
        del nw_dictionary['height']
        return nw_dictionary

    @property
    def size(self):
        """Get Return size """
        return self.width

    @size.setter
    def size(self, value):
        """Setter size value """
        self.width = value
        self.height = value

    def __str__(self):
        """Method str show objects"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    def update(self, *args, **kwargs):
        """update square public method"""
        if len(args) > 2:
            args = list(args)
            args.insert(2, args[1])

        cpy_kw = kwargs.copy()

        for key, value in cpy_kw.items():
            if key == 'size':
                kwargs[key] = value
                kwargs[key] = value
        Rectangle.update(self, *args, **kwargs)
