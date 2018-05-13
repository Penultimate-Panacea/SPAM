# encoding='utf-8'
def poem_from_file_path(file_path):
    """Reads a poem from a file into the program """
    from re import match
    file_path = file_path.lower()
    print(file_path)
    file_extension = match("\.(.*)", file_path)
    print(file_extension)
    if file_extension == ".poem":
        result = poem_from_poem(file_path)
        return result
    elif file_extension == ".txt":
        result = poem_from_text(file_path)
        return result
    else:
        print("That file type is not supported at the moment")
        quit(4)


def poem_from_example(exampletype, includemeta=0):
    """Reads a poem from ExamplePoetry Directory"""
    poemfiles = {"cinquain": "ExamplePoetry/Cinquain.txt", "haiku": "ExamplePoetry/Haiku.txt", "nonet":
                 "ExamplePoetry/Nonet.txt", "italysonnet": "ExamplePoetry/SonnetItaly.txt", "shakesonnet":
                 "ExamplePoetry/SonnetShake.txt"}
    metafiles = {"cinquain": "ExamplePoetry/Cinquain.meta", "haiku": "ExamplePoetry/Haiku.meta", "nonet":
                 "ExamplePoetry/Nonet.meta", "italysonnet": "ExamplePoetry/SonnetItaly.meta", "shakesonnet":
                 "ExamplePoetry/SonnetShake.meta"}
    selection = exampletype.lower()
    file = open(poemfiles[selection], 'r')
    poem = file.read().splitlines()
    file.close()
    if includemeta == 1:
        file = open(metafiles[selection], 'r')
        meta = file.read().splitlines()
        file.close()
        return poem, meta
    return poem


def poem_from_poem(file_path, includemeta=0):
    """Reads custom .poem file"""
    file = open(file_path, 'r')
    contents = file.read().splitlines()
    file.close()
    if includemeta == 1:
        meta = contents[0:3]
        poem = contents[3:]
        return poem, meta
    else:
        return contents[3:]


def poem_from_text(file_path, includemeta=0):
    if includemeta == 1:
        file = open(file_path, 'r')
        poem = file.read().splitlines()
        file.close()
        meta_path = input("Please specify path to .meta file, if no meta dat file exists.")
        meta = open(meta_path, 'r')
        metadata = meta.read().splitlines()
        meta.close()
        return poem, metadata
    else:
        file = open(file_path, 'r')
        poem = file.read().splitlines()
        file.close()
        return poem

def strip_punct(poem):
    """Removes all punctuation marks from poem"""
    from re import split
    from string import punctuation
    strippedpoem = []
    for line in poem:
        words = [split(' ', line)]
        strippedlinelist = []
        for word in words[0]:
            stripper = str.maketrans(dict.fromkeys(punctuation))
            strippedlinelist.append(word.translate(stripper))
            strippedline = ' '.join(strippedlinelist)
        strippedpoem.append(strippedline)
    return strippedpoem
