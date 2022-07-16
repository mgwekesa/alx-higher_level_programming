#!/usr/bin/python3

def read_file(filename=""):
    """ reads the file, and prints it to stdout """
    with open(filename, mode='r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
