from collections import OrderedDict

def neuralize(data):
    nodes = list(OrderedDict.fromkeys(data))  # Get unique characters preserving order
    base = len(nodes)
    key = 0

    for char in data:
        key = key * base + nodes.index(char) + 1

    cypher = f'{len(data)}..{key}..' + ''.join(nodes)
    # print(cypher)
    return cypher

def deneuralize(cypher):
    data_len, key, nodes = cypher.split('..')
    data_len = int(data_len)
    key = int(key)
    nodes = list(nodes)
    base = len(nodes)

    data = []
    for _ in range(data_len):
        key -= 1  # Convert key to zero-based index
        index = key % base
        data.append(nodes[index])
        key //= base

    data.reverse()
    print(''.join(data))
    return ''.join(data)
