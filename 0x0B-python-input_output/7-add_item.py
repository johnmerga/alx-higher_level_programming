#!/usr/bin/python3
'''  a script that appends all it's arguments to the add_item.json file '''
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    filename = 'add_item.json'
    ls = []
    try:
        ls = load_from_json_file(filename)
    except:
        pass
    ls.extend(sys.argv[1:])
    save_to_json_file(ls, filename)
