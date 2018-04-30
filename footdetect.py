# encoding='utf-8'
def wordstress(word):
    """Detects if syllables in a word are stressed, returns list of integers where 0 is unstressed and 1 is stressed"""
    #TODO: add support for multiple pronouciation
    #TODO: This is super slow, needs optimized
    from nltk.corpus import cmudict
    word = word.lower()
    pro_dict = cmudict.dict()
    try:
        pro = pro_dict[word][0]
        return [i[-1] for i in pro if i[-1].isdigit()]
    except KeyError:
        print("\nThat word does not exist in the current dictionary")
        quit(5)


def linestress(line):
    """Splits a line into words and creates a list of the stresses"""
    from re import split
    words = split(" ", line)
    stresses = []
    for i in words:
        stresses.append(wordstress(i))
    print(stresses)
    stressl = []
    for sublist in stresses:
        for item in sublist:
            stressl.append(item)
    print(stressl)
    return stressl


def classicalmeter(stressword):
    if len(stressword) == 1:
        foot = "none"
    elif len(stressword) == 2:
        feet = {['0', '0']: "pyrrhus", ['0', '1']: "iamb", ['1', '0']: "trochee", ['1', '1']: "spondee"}
        foot = feet[stressword]
    elif len(stressword) == 3:
        feet = {['0', '0', '0']: "tribach", ['1', '0', '0']: "dactyl", ['0', '1', '0']: "amphibrach", ['0', '0', '1']:
                "anapest", ['0', '1', '1']: "bacchius", ['1', '0', '1']: "cretic", ['1', '1', '0']: "antibacchius",
                ['1', '1', '1']: "molossus"}
        foot = feet[stressword]
    elif len(stressword) == 4:
        feet = {['0', '0', '0', '0']: "tetrabrach", ['1', '0', '0', '0']: "primus paeon", ['0', '1', '0', '0']:
                "secundus paeon", ['0', '0', '1', '0']: "tertius paeon", ['0', '0', '0', '1']: "quartus paeon",
                ['1', '1', '0', '0']: "major ionic", ['0', '0', '1', '1']: "minor ionic", ['1', '0', '1', '0']:
                "ditrochee", ['0', '1', '0', '1']: "diiamb", ['1', '0', '0', '1']: "choriamb", ['0', '1', '1', '0']:
                "antispast", ['0', '1', '1', '1']: "first epitrite", ['1', '0', '1', '1']: "second epitrite",
                ['1', '1', '0', '1']: "third epitrite", ['1', '0', '0', '0']: "fourth epitrite", ['1', '1', '1', '1']:
                "dispondee"}
        foot = feet[stressword]
    elif len(stressword) > 4:
        print("Word Length is not yet supported")
        quit(4)
    else:
        print("Invalid Input to the classicalmeter function")
        quit(6)
    return foot


print(classicalmeter(linestress("High above the tree ripe cherries sit")))

quit(0)