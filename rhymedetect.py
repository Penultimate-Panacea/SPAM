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


def schema_detect(poem):
    """
    Determines the rhyme schema from a rhymes and a linecount
    Unsure if it is better to go for a general solution that grows by n! or a set one that grows linearly
    """
    terminalwords = []
    for line in poem:
        schema = str('No Ryhme Scheme Detected')
        terminalword = line[-1]
        terminalwords.append(terminalword)
    for i in terminalwords:
        if twowordci(i,terminalwords[i+1]) == True and twowordci(i, terminalwords[i+2]) == False:
            # Ryhme Scheme = RR X ...
        elif twowordci(i,i+1) == False and twowordci(i, terminalwords[i+2]) == True:
            # Rhyme Scheme = RXRX ...

