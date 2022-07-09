#!/usr/bin/python3

def uppercase(str):
    str_upp = ""
    for c in str:
        if (c >= 'a' and c <= 'z'):
            c = chr(ord(c) - 32)
        str_upp += c
    print("{:s}".format(str_upp))
