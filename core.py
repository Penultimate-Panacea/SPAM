# encoding='utf-8'
import importpoem
import footdetect
from nltk.corpus import cmudict
from tqdm import tqdm
rawpoem = importpoem.poem_from_example("Haiku")
poem = importpoem.strip_punct(rawpoem)
print(poem, "\n")
meter = []
print("Analysing Stress:")
print("\n")
linestresses = []
for line in tqdm(poem):
    linestresses.append(footdetect.linestress(line, pro_dict = cmudict.dict()))
linestresses = linestresses[0] #FIXME: It is getting wrapped twice for some reason
for stress in linestresses:
    stress = tuple(stress)
print("\n", linestresses)


