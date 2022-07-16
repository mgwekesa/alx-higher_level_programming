#!/usr/bin/python3

""" writes a string to a text file """


def write_file(filename="", text=""):
    """ returns the number of characters written """
    with open(filename, mode='w') as f:
        return f.write(text)
