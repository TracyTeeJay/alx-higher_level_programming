#!/usr/bin/python3

def uniq_add(my_list=[]):

    set_list = set(my_list)

    sum = 0
    for ints in set_list:
        sum += ints

    return (sum)
