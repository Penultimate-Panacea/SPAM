# encoding='utf-8'
def wordstress(word):
    """Detects if syllables in a word are stressed, returns list of integers where 0 is unstressed and 1 is stressed"""
    # TODO: This is super slow, needs optimized
    from nltk.corpus import cmudict
    word = word.lower()
    pro_dict = cmudict.dict()
    try:
        pro = pro_dict[word][0]  # TODO: add support for multiple pronouciation
        return tuple(i[-1] for i in pro if i[-1].isdigit())  # Not sure what this does, but it makes it work
    except KeyError:
        print("The word:", word, "does not exist in the current dictionary")
        quit(3)


def linestress(line):
    """Splits a line into words and creates a list of the stresses"""
    from re import split, sub
    words = split(" ", line)
    stresses = []
    for i in words:  # tuple to list
        rawstresses = wordstress(i)
        list(rawstresses)
        cleanstresses = []
        for j in rawstresses:
            cleanstress = sub('2', '1', j)
            cleanstresses.append(cleanstress)
        tuple(cleanstresses)
        stresses.append(cleanstresses)  # and back again
    return stresses


def makeblocks(line):
    """Determines the number of feet and passes it to classicalmeter()"""
    pass

def classicalclassify(block):
    """classifies a tuple of stresses as """
    if len(block) == 1:
        foot = "none"
        return foot
    elif len(block) == 2:
        feet = {('0', '0'): "pyrrhus", ('0', '1'): "iamb", ('1', '0'): "trochee", ('1', '1'): "spondee"}
        foot = feet[tuple(block)]
        return foot
    elif len(block) == 3:
        feet = {('0', '0', '0'): "tribach", ('1', '0', '0'): "dactyl", ('0', '1', '0'): "amphibrach", ('0', '0', '1'):
                "anapest", ('0', '1', '1'): "bacchius", ('1', '0', '1'): "cretic", ('1', '1', '0'): "antibacchius",
                ('1', '1', '1'): "molossus"}
        foot = feet[tuple(block)]
        return foot
    elif len(block) == 4:
        feet = {('0', '0', '0', '0'): "tetrabrach", ('1', '0', '0', '0'): "primus paeon", ('0', '1', '0', '0'):
                "secundus paeon", ('0', '0', '1', '0'): "tertius paeon", ('0', '0', '0', '1'): "quartus paeon",
                ('1', '1', '0', '0'): "major ionic", ('0', '0', '1', '1'): "minor ionic", ('1', '0', '1', '0'):
                    "ditrochee", ('0', '1', '0', '1'): "diiamb", ('1', '0', '0', '1'): "choriamb", ('0', '1', '1', '0'):
                    "antispast", ('0', '1', '1', '1'): "first epitrite", ('1', '0', '1', '1'): "second epitrite",
                ('1', '1', '0', '1'): "third epitrite", ('1', '0', '0', '0'): "fourth epitrite", ('1', '1', '1', '1'):
                    "dispondee"}
        foot = feet[tuple(block)]
        return foot
    elif len(block) > 4:
        print("Word Length is not yet supported")
        print(block)
        quit(4)
    else:
        print("Invalid Input to the classicalmeter function")
        quit(6)


def temp_test():
    print(linestress("Two households both alike in dignity"))
    for word in linestress("Two households both alike in dignity"):
        print(classicalclassify(word))



