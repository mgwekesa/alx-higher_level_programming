#!/usr/bin/python3

""" a function that prints a square with the character '#' """


def print_square(size):
    """
    size is the length of the square

    Return:
        None
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
