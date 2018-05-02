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
