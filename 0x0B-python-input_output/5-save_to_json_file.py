#!/usr/bin/python3
''' module for the save_to_json_file() function '''
import json


def save_to_json_file(my_obj, filename):
    ''' saves an object's json string to a file '''
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
