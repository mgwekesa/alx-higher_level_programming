#!/usr/bin/python3

def islower(c):
    for letter in range(97, 123):
        if (c == chr(letter)):
            return (True)
    else:
        return (False)
