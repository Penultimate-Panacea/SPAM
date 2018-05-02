# encoding='utf-8'


def twowordperfect(word1, word2):
    """Two word rhyme non perfect detection, returns bool"""
    from pronouncing import rhymes
    rhymesword1 = rhymes(word1)
    rhymesword2 = rhymes(word2)
    for value in rhymesword1:
        if value in rhymesword2:
            rhymes = True
            return rhymes
    rhymes = False
    return rhymes

