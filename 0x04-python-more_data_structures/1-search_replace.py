#!/usr/bin/python3

def search_replace(my_list, search, replace):
    srch_replc = []

    for ints in my_list:
        if ints == search:
            srch_replc.append(replace)
        else:
            srch_replc.append(ints)
    return srch_replc
