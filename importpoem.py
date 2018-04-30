def poem_from_file(file_path):
    """Reads a poem from a file into the program """
    from re import sub
    file = open(file_path, 'r')
    poem = file.read().splitlines()
    file.close()
    return poem

def poem_from_example(type, includemeta = 0):
    """Reads a poem from ExamplePoetry Directory"""
    poemfiles = {"cinquain": "ExamplePoetry/Cinquain.txt", "haiku": "ExamplePoetry/Haiku.txt", "nonet":
            "ExamplePoetry/Nonet.txt"}
    metafiles = {"cinquain": "ExamplePoetry/Cinquain.meta", "haiku": "ExamplePoetry/Haiku.meta", "nonet":
            "ExamplePoetry/Nonet.meta"}
    selection = type.lower()
    file = open(poemfiles[selection], 'r')
    poem = file.read().splitlines()
    file.close()
    if includemeta == 1:
        file = open(metafiles[selection], 'r')
        meta = file.read().splitlines()
        file.close()
        return poem, meta
    return poem