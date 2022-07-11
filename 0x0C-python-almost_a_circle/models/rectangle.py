#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """ class for the rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing attributes """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """ getter and setter for width """
    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        self.__width = value

    """ getter and setter for height """
    @property
    def height(self):
        """ getter for width """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        self.__height = value

    """ getter and setter for x """
    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        self.__x = value

    """ getter and setter for y """
    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y """
        self.__y = y
