#!/usr/bin/python3

"""
returns True if the object of an instance of, or if the
object is an instance of a class that inherited from,
the specified class; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
        Returns:
            True if obj is instance of a_class, else False
    """

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
