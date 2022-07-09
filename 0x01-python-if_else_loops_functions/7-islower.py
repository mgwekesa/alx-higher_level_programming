#!/usr/bin/python3

def islower(c):
    for letter in range(97, 123):
        if (c == chr(letter)):
            return (True)
    for letter in range(65, 91):
        if (c == (letter)):
            return (False)
