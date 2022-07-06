#!/usr/bin/python3

""" returns True if the object is exactly an instance of the
    specified class; otherwise False
"""


def is_same_class(obj, a_class):
    """
    checks whether obj is an exact instance of the class given

    Returns:
        True if obj is an instance of a_class, else False
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
