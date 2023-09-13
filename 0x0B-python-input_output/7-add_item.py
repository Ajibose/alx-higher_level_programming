#!/usr/bin/python3
"""Define a function add all the file arguments to a python list"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

save_to_json_file(sys.argv[1:], "add_item.json")
