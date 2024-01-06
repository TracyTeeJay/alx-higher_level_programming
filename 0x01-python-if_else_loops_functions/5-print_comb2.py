#!/usr/bin/python3

"""
function that prints numbers in hexadecimal
"""

for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
