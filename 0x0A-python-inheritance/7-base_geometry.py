#!/usr/bin/python3

""" BaseGeometry class """


class BaseGeometry:
    """ Exception raised by public instance method, area """
    def area(self):
        raise Exception("area() is not implemented")
    """ Public instance method integer_validator validates integer """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
