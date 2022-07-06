#!/usr/bin/python3

""" class MyList that inherits from list """


class MyList(list):
    """ Public instance method, def print_sorted(self) """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        Assume all the elements of the list will be of type int
        """
        for item in self:
            if type(item) != int:
                raise TypeError("The list must contain integer elements")
        print(sorted(self))
