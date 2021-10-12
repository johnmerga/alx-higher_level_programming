#!/usr/bin/python3
''' module for the append_after() function '''


def append_after(filename="", search_string="", new_string=""):
    ''' appends new_string after every match of search_string in filename'''
    s = ''
    with open(filename, 'r+') as file:
        lns = file.readlines()
        for ln in lns:
            s += ln + (new_string if search_string in ln else '')
        file.seek(0)
        file.write(s)
