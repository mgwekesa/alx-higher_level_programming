#!/usr/bin/python3
""" base class """
import json
from os import path


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

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        """ json_string is representing a list of dictionaries """
        if json_string is None or json_string == "":
            return []
        list_dic = json.loads(json_string)
        return list_dic

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        """
        **dictionary is a double pointer dictionary
        to use update method to assign all attributes
        - create a Rectangle instance with 'dummy' mandatory attributes,
        - call update instance method to this 'dummy' to apply real values
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(6, 10)
        if cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        new_list = []

        file_n = cls.__name__ + ".json"
        if path.exists(file_n):
            with open(file_n, encoding='utf-8') as f:
                list_dic = cls.from_json_string(f.read())
            for dic in list_dic:
                new_list.append(cls.create(**dic))
        return new_list
