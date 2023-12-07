#!/usr/bin/python3

"""
function to append text and output number of characters in appednment
"""


def append_write(filename="", text=""):
    """
    returns number characters in appended string
    Args:
    filename (str): name of file
    text (str): text to be appended
    """
    if not isinstance(text, str):
        return 0
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)

    return len(text)
