#!/usr/bin/python3

""" Function prints 'My name is <first name> <last name'"""


def say_my_name(first_name, last_name=""):
    """
    the function takes two parameters, first_name and last_name
    first_name is an mandatory parameter, last_name an optional one

    return:
        None
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
