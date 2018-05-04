# encoding='utf-8'
import importpoem
import footdetect
from tqdm import tqdm
rawpoem = importpoem.poem_from_example("Haiku")
poem = importpoem.strip_punct(rawpoem)
meter = []
print("Analysing Stress:")
for line in tqdm(poem):
    linestresses = []
    linestresses.append(footdetect.linestress(line))
linestresses = linestresses[0] #FIXME: It is getting wrapped twice for some reason
print(poem)
print(linestresses)


