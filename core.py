# encoding='utf-8'
import importpoem
import footdetect
from tqdm import tqdm
poem = importpoem.poem_from_example("nonet")
print(poem)
for line in tqdm(poem):
    for word in footdetect.linestress("Two households both alike in dignity"):
        print("\n", footdetect.classicalmeter(word))

