# encoding='utf-8'
import importpoem
import footdetect
from tqdm import tqdm
poem = importpoem.poem_from_example("shakesonnet")
#poem = importpoem.strip_punct(poem)
meter = []
for line in tqdm(poem):
    linestresses = []
    linestresses.append(footdetect.linestress(line))
    for stress in linestresses:
        classicfoot = footdetect.classicalmeter(stress) #Currently passing lol to function, needs tuples
        meter.append(classicfoot)
print(meter)


