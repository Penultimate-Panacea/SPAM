# encoding='utf-8'
def wordstress(word):
    """Detects if syllables in a word are stressed, returns list of integers where 0 is unstressed and 1 is stressed"""
    #TODO: add support for multiple pronouciation
    from nltk.corpus import cmudict
    word = word.lower()
    pro_dict = cmudict.dict()
    try:
        pro = pro_dict[word][0]
        return [i[-1] for i in pro if i[-1].isdigit()]
    except KeyError:
        print("\nThat word does not exist in the current dictionary")

def linestress(line):
    """Splits a line into words and creates a list of the stresses"""
    from re import split
    words = split(" ", line)
    stresses = []
    for i in words:
        stresses.append(wordstress(i))
    stressl = []
    for sublist in stresses:
        for item in sublist:
            stressl.append(item)

    return stressl

def isiamb(syls):
    """Detects if a foot is an iamb [uS], returns bool"""

def istrochee(syls):
    """Detects if a foot is an trochee [Su], returns bool"""

def isanapest(syls):
    """Detects if a foot is an anapest [uuS], returns bool"""

def isdactyl(syls):
    """Detects if a foot is an dactyl [Suu], returns bool"""


print(linestress("High above the tree ripe cherries sit"))
quit(0)