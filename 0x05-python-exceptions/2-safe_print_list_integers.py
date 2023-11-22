#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    itemsNo = 0
    for cnt in range(x):
        try:
            print("{:d}".format(my_list[cnt]), end="")
            itemsNo += 1
        except (ValueError, TypeError):
            continue
    print()
    return itemsNo
