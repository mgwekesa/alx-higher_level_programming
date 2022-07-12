#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """ class for the rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing attributes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ getter and setter for width """
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
            if value <= 0:
                raise ValueError("width must be > 0")
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
            if (value <= 0):
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    """ getter and setter for x """
    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    """ getter and setter for y """
    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance """
        return (self.height * self.width)

    def display(self):
        """ prints in stdout the Rectangle instance with character # """
        for n in range(self.y):
            print()
        for index in range(self.height):
            print("".join(" " for j in range(self.x)), end="")
            print("".join(["#" for k in range(self.width)]))

    def __str__(self):
        """ overides the string method """
        ret = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return (ret.format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ assigns a key/value argument to each attribute """
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

        """ assigns a key/value argument to attributes """
        """ 'key-worded argument' can be ignored if args has been used """
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "width" in kwargs:
            self.width = kwargs["width"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]
