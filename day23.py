import networkx as nx

with open('input/23.txt') as f:
    lines = [line.rstrip() for line in f]

network_map = nx.Graph()
for this_line in lines:
    comp1, comp2 = tuple(this_line.split('-'))
    network_map.add_edge(comp1, comp2)

all_cliques = list(nx.enumerate_all_cliques(network_map))
triad_cliques = [x for x in all_cliques if len(x) == 3]

triads_with_t = 0
for this_triad in triad_cliques:
    for this_node in this_triad:
        if this_node.startswith('t'):
            triads_with_t += 1
            break
print(f"Part 1: {triads_with_t}")

largest_cluster = all_cliques[-1]
lan_password = ''
for computer_name in sorted(largest_cluster):
    lan_password += computer_name + ','
lan_password = lan_password[:-1]
print(f"Part 2: {lan_password}")
