import math
from collections import OrderedDict


def neuralize(data):
    nodes = list(''.join(OrderedDict.fromkeys(data)))
    layers = 1
    for i, char in enumerate(data):
        if i == 0: continue
        layers = layers * len(nodes) - (len(nodes) - (nodes.index(char) + 1))
        #           layers                                 Range      Key                        Nodes
    cypher = f'{len(data)}.{int(math.pow(len(nodes),len(data)))}.{layers}.{''.join( n for n in nodes )}'
    return cypher

def denueralize(cypher):
    cypher = cypher.split(".")
    layers = int(cypher[0])
    ranges = int(cypher[1])
    key = int(cypher[2])
    nodes = list(cypher[3])
    
    data = []
    for _ in range(1, layers + 1):
        ranges = ranges // len(nodes)
        data.append(nodes[((key - 1) // ranges) % len(nodes)])
    print("text: ", end="")
    print(*data, sep="")
