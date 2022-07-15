#!/usr/bin/python3
""" base class """
import json


class Base:
    """ class for base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing the base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        file_n = cls.__name__ + ".json"
        list_dict = []

        if list_objs is not None:
            for i in list_objs:
                list_dict.append(i.to_dictionary())

        j_str = cls.to_json_string(list_dict)

        with open(file_n, mode='w') as f:
            f.write(j_str)
