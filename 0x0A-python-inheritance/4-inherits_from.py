#!/usr/bin/python3

"""
returns True if the object is an instance of class that inherited
(directly or indirectly) from the specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Returns:
        True if isinstance(obj, a_class), else False
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False)
