#!/usr/bin/python3
''' module for the append_file() function '''


def append_write(filename="", text=""):
    ''' appends text to a file '''
    with open(filename, 'a') as file:
        return file.write(text)
