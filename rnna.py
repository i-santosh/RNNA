import math

from collections import OrderedDict


def get_nodes(data):
    return list(''.join(OrderedDict.fromkeys(data)))


def get_iterations_to_reach_char(nodes, target_char, char_depth):
    # Calculate the number of times the character list is cycled through
    iterations = char_depth * len(nodes) - 1
    
    # Adjust if the target character is not the first character in the list
    char_index = nodes.index(target_char)
    iterations += char_index
    # print(iterations)
    return iterations


def neuralize(data):
    print(data)
    nodes = sorted(get_nodes(data))

    char_depth = 1
    for char in data:
        char_depth = get_iterations_to_reach_char(nodes, char, char_depth)
        #  l d e n    length depth endpoint nodes
    cypher = f'{len(data)}.{int(math.pow(len(nodes),len(data)))}.{char_depth}.{''.join( n for n in nodes )}'
    print(cypher)
    return cypher


def find_character(number, range_size, nodes):
    # Determine the index of the character that gets the specified number
    index = (number - 1) // range_size
    
    # Get the character from the list
    character = nodes[index % len(nodes)]
    
    return character

def denueralize(cypher):
    cypher = cypher.split(".")

    length = int(cypher[0])
    depth = int(cypher[1])
    endpoint = int(cypher[2])
    nodes = list(cypher[3])
    data = []
    for i in range(1, length+1):
        data.append(find_character(endpoint, depth, nodes))
        depth = depth // len(nodes)
    data.reverse()
    print(''.join(char for char in data))



while True:
    try:
        data = input("Enter Text: ")
        neuralize(data)
        cypher = input("Enter cypher: ")
        denueralize(cypher)
    except KeyboardInterrupt:
        print("Exiting...")
        break
