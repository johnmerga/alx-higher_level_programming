#!/usr/bin/python3
''' module for the class_to_json() function '''


def class_to_json(obj):
    ''' converts a class instance to a json string '''
    return obj.__dict__.copy()
