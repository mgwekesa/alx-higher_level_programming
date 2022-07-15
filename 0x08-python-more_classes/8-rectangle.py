#!/usr/bin/python3
""" Rectangle class with several methods """


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width, height):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                str_rec += str(self.print_symbol)
            if row < self.__height - 1:
                str_rec += "\n"
        return str_rec

    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle(%s, %s)" % (self.__width, self.__height)

    def __del__(self):
        """ prints the message 'Bye rectangle...' when instance deleted """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the equality of two rectangles based on area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
