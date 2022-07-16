#!/usr/bin/python3

""" This reads the file, using the optional mode 'r'"""


def read_file(filename=""):
    """ reads the file, and prints it to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
