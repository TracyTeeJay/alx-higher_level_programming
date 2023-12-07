#!/usr/bin/python3

"""
function that writes text string to a file and returns number of characters
"""


def write_file(filename="", text=""):
    """
    returns created file and number of cahracters
    args:
    filename (str): name of file
    text (str): content of file
    """
    nbCharacters = 0
    if not isinstance(text, str):
        return nbCharacters

    with open(filename, "w", encoding="utf=8") as file:
        nbCharacters = file.write(text)

    return nbCharacters
