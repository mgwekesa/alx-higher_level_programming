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
        self.size = size

    def area(self):
        """
        Public instance method

        Returns: the current square area
        """
        return (self.size * self.size)

    def my_print(self):
        """
        Public instance method

        Prints in stdout the square with the character #

        Returns:
            None
        """
        if self.size == 0:
            print()
            return
        for index in range(self.size):
            print("".join(["#" for j in range(self.size)]))

    @property
    def size(self):
        """
        getter of __size

        Retrieves the size private attribute for the setter

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter of __size

        Args:
            value(int): the size of the square

        Property setter to set the value of the private attribute

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
