#!/usr/bin/python3
""" Rectangle class with several methods """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width, height):
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

    """ getter and setter for height """
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
        return self.__width * self.__height

    """ instance method for perimeter """
    def perimeter(self):
        """ returns the perimeter """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2*(self.__width + self.__height)

    """ using print() and str() to print the rectangle """
    def __str__(self):
        """ returns the rectangle with the character '#' """
        str_rec = ""
        if (self.__width == 0 or self.__height == 0):
            return str_rec

        for row in range(self.__height):
            for col in range(self.__width):
                str_rec += "#"
            if row < self.__height - 1:
                str_rec += "\n"
        return str_rec

    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle(%s, %s)" % (self.__width, self.__height)
