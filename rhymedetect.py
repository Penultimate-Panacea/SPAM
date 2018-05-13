# encoding='utf-8'
def twowordci(word1, word2):
    """Two word rhyme context independent[for all pronunciations] detection, returns bool"""
    from pronouncing import rhymes
    rhymesword1 = rhymes(word1)
    rhymesword2 = rhymes(word2)
    for value in rhymesword1:
        if value in rhymesword2:
            isrhyme = True
            return isrhyme
    isrhyme = False
    return isrhyme


def schema_detect(rhymes, linecount):
    """
    Determines the rhyme schema from a rhymes and a linecount
    Unsure if it is better to go for a general solution that grows by n! or a set one that grows linearly
    """
