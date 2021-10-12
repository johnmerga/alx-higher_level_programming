#!/usr/bin/python3
''' module for the read_file() function '''


def read_file(filename=""):
    ''' prints the contents of a file '''
    with open(filename) as file:
        print(file.read(), end='')
