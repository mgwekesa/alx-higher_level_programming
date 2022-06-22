#!/usr/bin/python3

""" Defines the class Square that defines a square"""


class Square:
    """
    Square class

    Attributes:
    __size (int): size of the side of a square
    __position (tuple): position of the square in 2D
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square

        Args:
            size (int): size of the size of a square

        Returns: None
        """
        self.size = size
        self.position = position

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
        for i in range(self.position[1]):
            print()
        for index in range(self.size):
            print("".join(" " for j in range(self.position[0])), end="")
            print("".join(["#" for k in range(self.size)]))

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

    @property
    def position(self):
        """
        getter of the position

        Retrieves the position private attribute for the setter

        Returns:
            the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter of __position

        Args:
            value (tuple): position of the square in 2D
        Returns:
            None
        """
        err_msg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError(err_msg)
        else:
            self.__position = value

    def __str__(self):
        """
        Printing the square instance using string representation

        Returns:
            Formatted string representation of the square
        """

        add = (" " * self.position[0] + "#" * self.size + "\n")
        if self.size == 0:
            return ""
        str_rep = "\n" * self.position[1] + add * self.size
        return str_rep[:-1]
