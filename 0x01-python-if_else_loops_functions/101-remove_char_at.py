#!/usr/bin/python3

def remove_char_at(str, n):
    cpy_str = []
    cpy = ""
    for char in str:
        cpy_str.append(char)
    for i in range(len(cpy_str)):
        if (i == n):
            cpy_str.pop(i)
    for i in cpy_str:
        cpy += i
    return cpy
