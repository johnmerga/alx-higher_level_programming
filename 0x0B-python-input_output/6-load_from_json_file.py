#!/usr/bin/python3
''' module for the load_from_json_file() function '''
import json


def load_from_json_file(filename):
    ''' loads an object from a json string file '''
    with open(filename, 'r') as file:
        return json.load(file)
