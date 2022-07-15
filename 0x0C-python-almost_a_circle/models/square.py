#!/usr/bin/python3
""" Square class inheriting from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializing the square class """
        self.size = size
        super().__init__(size, size, x, y, id)

    """ getter and setter for size """
    @property
    def size(self):
        """ getter for size """
        return self.__width

    @size.setter
    def size(self, size):
        """ setter for size """
        super().validate("width", size)
        self.__width = size
        self.__height = size

    def __str__(self):
        ret = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return (ret.format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ assigns attributes """
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
    """ if *args exist, **kwargs are skipped """
    """ **kwargs are a double pointer to a dictionary """
