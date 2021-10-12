#!/usr/bin/python3
''' module for the write_file() function '''


def write_file(filename="", text=""):
    ''' writes to a file '''
    with open(filename, 'w') as file:
        return file.write(text)
