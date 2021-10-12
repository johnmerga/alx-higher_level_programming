#!/usr/bin/python3
''' module for the Student class '''


class Student:
    ''' Student data class '''
    def __init__(self, first_name, last_name, age):
        ''' instantiates a student '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' return json dict of the student '''
        return self.__dict__.copy()
