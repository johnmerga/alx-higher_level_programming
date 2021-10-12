#!/usr/bin/python3
''' module for the to_json_string() function '''
import json


def to_json_string(my_obj):
    ''' converts an object into a json string '''
    return json.dumps(my_obj)
