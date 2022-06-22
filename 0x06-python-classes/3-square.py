#!/usr/bin/python3

""" Defines the class Square that defines a square"""


class Square:
    """
    Square class

    Attributes:
    __size (int): size of the side of a square
    """

    def __init__(self, size=0):
        """
        Initializes the square

        Args:
            size (int): size of the size of a square

        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """
        Public instance method

        Returns: the current square area
        """
        return (self.__size * self.__size)
