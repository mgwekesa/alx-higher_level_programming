#!/usr/bin/python3
""" Rectangle class with area and perimeter instance methods """


class Rectangle:
    """  Rectangle class """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ getters and setters for width """
    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    """ getter and setter for height"""
    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    """ instance method for area """
    def area(self):
        """ returns the area """
        return self.__height * self.__width

    """ instance method for perimeter """
    def perimeter(self):
        """ returns the perimeter """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__height + self.__width)
