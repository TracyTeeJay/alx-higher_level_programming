#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_list = []

    for cnt in range(len(my_list) - 1, -1, -1):
        new_list.append(my_list[cnt])

    for items in new_list:
        print("{:d}".format(items))
