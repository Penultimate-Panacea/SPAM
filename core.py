# encoding='utf-8'
def count_syl(line):
    """Creates a dictionary that relates each word in a line to the number of syllables in that word"""
    from pyphen import Pyphen
    from re import split
    dic = Pyphen(lang='en-US')
    words = split(" ", line)
    syllables = {}
    j = 0
    for i in words:
        syllables[i] = len(split("-", dic.inserted(words[j])))
        j += 1
    return syllables


def poem_from_file(file_path):
    """Reads a poem from a file into the program """
    file = open(file_path, 'r')
    poem = file.readlines()
    file.close()
    return poem


def line_assoc(poem):
    """Creates the structure to add attributes to each line of the poem"""


