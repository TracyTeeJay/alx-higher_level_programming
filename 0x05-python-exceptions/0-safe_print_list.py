#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    itemsNo = 0
    try:
        for cnt in my_list:
            if itemsNo == x:
                print()
                return itemsNo

            print("{}".format(cnt), end="")
            itemsNo += 1
    except Exception:
        print()
        return itemsNo
    print()
    return itemsNo
