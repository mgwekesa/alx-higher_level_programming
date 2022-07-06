#!/usr/bin/python3

""" returns the list of available attributes and methods of an object """


def lookup(obj):
    """
    0-lookup.py
    takes the object as an attribute

    Returns:
        list object
    """
    return (dir(obj))
