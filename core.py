# encoding='utf-8'
from nltk.corpus import cmudict
from tqdm import tqdm

import footdetect
import importpoem

rawpoem = importpoem.poem_from_file_path("This.poem")
poem = importpoem.strip_punct(rawpoem)
print(poem, "\n")
meter = []
print("Analysing Stress:")
print("\n")
linestresses = []
for line in tqdm(poem):
    linestresses.append(footdetect.linestress(line, pro_dict=cmudict.dict()))
for stress in linestresses:
    stress = tuple(stress)
print("\n", linestresses[0])  # FIXME: There should be only one layer on this list
