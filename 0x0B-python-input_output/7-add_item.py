#!/usr/bin/python3

"""
function that writes object to text form using json format
and creates object from json file
"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
new_list_items = sys.argv[1:]
items = []

try:
    file = open(filename, "r")
    cntnt = file.read()
    file.close()
    if len(cntnt):
        items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

for item in new_list_items:
    items.append(item)

save_to_json_file(items, filename)
