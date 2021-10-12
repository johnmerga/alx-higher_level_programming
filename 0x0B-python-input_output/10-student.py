#!/usr/bin/python3
''' module for the Student class '''


class Student:
    ''' Student data class '''
    def __init__(self, first_name, last_name, age):
        ''' instantiates a student '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' return json dict of the student '''
        if type(attrs) is list and all(type(v) is str for v in attrs):
            return {v: self.__dict__[v] for v in self.__dict__ if v in attrs}
        return self.__dict__.copy()
