#!/usr/bin/python3
""" Square class inheriting from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    """ getter and setter for size """
    @property
    def size(self):
        """ getter for size """
        return self.__width

    @size.setter
    def size(self, value):
        """ setter for size """
        super().validate("width", value)
        self.__width = value
        self.__height = value

    def __str__(self):
        ret = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return (ret.format(self.id, self.x, self.y, self.width))
