#!/usr/bin/python3

"""
dictionary description with simple data structure
from JSON serialization of an object
"""
import json


def class_to_json(obj):
    """ returns the dictionary representation of class as JSON """
    return obj.__dict__
