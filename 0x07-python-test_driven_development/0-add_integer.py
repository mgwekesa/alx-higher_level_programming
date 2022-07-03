#!/usr/bin/python3

"""     function that adds two numbers, a and b """

def add_integer(a, b=98):
    """
    a is a mandatory argument, b is an optional argument

    Returns:
        a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)
