# encoding='utf-8'
def count_syl(line):
    """Creates a dictionary that relates each word in a line to the number of syllables in the line"""
    from pyphen import Pyphen
    from re import split
    dic = Pyphen(lang='en-US')
    words = split(" ", line)
    syllables = {}
    j = 0
    if line == '':
        return -1
    else:
        for i in words:
            syllables[i] = len(split("-", dic.inserted(words[j])))
            j += 1
        line_syl_count = int(sum(syllables.values()))
        return line_syl_count #Returns as int


def poem_from_file(file_path):
    """Reads a poem from a file into the program """
    from re import sub
    file = open(file_path, 'r')
    poem = file.read().splitlines()
    file.close()
    return poem


def classify_by_syl(syl_count):
    #TODO: Contine adding poem classifications
    from numpy import mean
    length = len(syl_count)
    if length == 5 and syl_count[0] == 2 and syl_count[1] == 4 and syl_count[2] == 6 and syl_count[3] == 8 and \
            syl_count[4] == 2 :
        form = "Cinquain"
    elif length == 9 and syl_count[0] == 9 and syl_count[1] == 8 and syl_count[2] == 7 and syl_count[3] == 6 and \
            syl_count[4] == 5 and syl_count[5] == 4 and syl_count[6] == 3 and syl_count[7] == 2 and syl_count[8] == 1:
        form = "Nonet"
    elif length == 3 and syl_count[0] == 5 and syl_count[1] == 7 and syl_count[2] == 5:
        form = "Haiku"
    elif length == 6:
        form = "Sextain"
    elif (length == 13 or length == 14) and mean(syl_count) == 8:
        form = "Formal French Rondel"
    else:
        form = "Open Form"
    return form
poemLines = poem_from_file("This.txt")
i = 0
j = 0
syls = poemLines[:]
for i in poemLines:
    syls[j] = count_syl(i)
    j += 1
print(poemLines)
print(syls)

