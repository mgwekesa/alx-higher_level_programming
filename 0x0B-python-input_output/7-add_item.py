#!/usr/bin/python3

""" adds all arguments to a Python list, and then save them to a file """
from sys import argv
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = 'add_item.json'

if path.isfile(file):
    new_list = load_from_json_file(file)
else:
    new_list = []
for i in range(1, len(argv)):
    new_list.append(argv[i])
save_to_json_file(new_list, file)
