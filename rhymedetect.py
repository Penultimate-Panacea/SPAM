"""Detects if two words count as rhyming"""
def twoword(word1, word2):
    """Two Word rhyme detection, returns bool"""
    from pronouncing import rhymes
    rhymesword1 = rhymes(word1)
    rhymesword2 = rhymes(word2)
    for value in rhymesword1:
        if value in rhymesword2:
            rhymes = True
            return rhymes
    rhymes = False
    return rhymes

