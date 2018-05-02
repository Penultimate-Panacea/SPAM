def poem_from_file(file_path):
    """Reads a poem from a file into the program """
    file = open(file_path, 'r')
    poem = file.read().splitlines()
    file.close()
    return poem


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


def strip_punct(poem):
    from re import split
    from string import punctuation
    strippedpoem = []
    for line in poem:
        words = []
        words.append(split(" ", line))
        strippedline = []
        print(words)
        for word in words[0]:
            print(word)
            #stripper = word.maketrans(punctuation, )
          #FIXME  word.translate(word, None[, punctuation])
        print(words)
        print(line)

    return strippedpoem