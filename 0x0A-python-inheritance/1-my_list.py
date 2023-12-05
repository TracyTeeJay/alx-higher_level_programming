#!/usr/bin/python3

"""
function to print element from list and sort them
"""


class MyList(list):
    """
    returns sorted list
    Args:
    """
    def print_sorted(self):
        """
        Prints list in sorted form
        """
        print(sorted(self.copy()))
