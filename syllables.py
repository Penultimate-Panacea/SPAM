def count_syl_line(line):
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
        return line_syl_count
