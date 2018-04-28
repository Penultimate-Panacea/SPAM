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
        return 0
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
    length = len(syl_count)
    if length == 5 and syl_count[0] == 2 and syl_count[1] == 4 and syl_count[2] == 6 and syl_count[3] == 8 and syl_count[4] == 2 :
        form = "Cinquain"
    else:
        form = "Freeform"
    return form
poemLines = poem_from_file("This.txt")
i = 0
j = 0
syls = poem[:]
for i in poem:
    syls[j] = count_syl(i)
    j += 1
print(poem)
print(syls)

