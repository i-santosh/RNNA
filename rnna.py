import math
from collections import OrderedDict


def neuralize(data):
    nodes = list(''.join(OrderedDict.fromkeys(data)))
    key = 1
    for i, char in enumerate(data):
        if i == 0: continue
        key = key * len(nodes) - (len(nodes) - (nodes.index(char) + 1))
        #           data_len                                Range      Key                        Nodes
    # cypher = f'{len(data)}.{int(math.pow(len(nodes),len(data)))}.{layers}.{''.join( n for n in nodes )}'
    cypher = f'{len(data)}..{key}..{''.join( n for n in nodes )}'
    print(cypher)
    return cypher

def deneuralize(cypher):
    cypher = cypher.split("..")

    data_len = int(cypher[0])
    key = int(cypher[1])
    nodes = list(cypher[2])

    ranges = int(math.pow(len(nodes), data_len))

    
    data = []
    for _ in range(1, data_len + 1):
        ranges = ranges // len(nodes)
        index = ((key - 1) // ranges)
        data.append(nodes[index % len(nodes)])
    print("text: ", end="")
    print(*data, sep="")


deneuralize(neuralize("The kernel serves as core operating system component that manages hardware resources."))
