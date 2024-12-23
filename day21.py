import networkx as nx
with open('input/21.txt') as f:
    lines = [line.rstrip() for line in f]

codes = []
for this_line in lines:
    codes.append(this_line)

"""
num_pad             dir_pad
+---+---+---+           +---+---+
| 7 | 8 | 9 |           | ^ | A |
+---+---+---+       +---+---+---+
| 4 | 5 | 6 |       | < | v | > |
+---+---+---+       +---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

"""

dir_pad = nx.DiGraph()
dir_pad.add_edges_from(
    [('^', 'A', {'dir': '>'}), ('A', '^', {'dir': '<'}), ('^', 'v', {'dir': 'v'}),
        ('v', '^', {'dir': '^'}), ('A', '>', {'dir': 'v'}), ('>', 'A', {'dir': '^'}),
        ('<', 'v', {'dir': '>'}), ('v', '<', {'dir': '<'}), ('v', '>', {'dir': '>'}),
        ('>', 'v', {'dir': '<'})])


"""
for c in "<>v^A":
    print(f"Edges from {c}: {list(nx.neighbors(dir_pad, c))}")
"""

num_pad = nx.DiGraph()
num_pad.add_edges_from(
    [(7, 8, {'dir': '>'}), (8, 7, {'dir': '<'}), (7, 4, {'dir': 'v'}), (4, 7, {'dir': '^'}),
        (8, 5, {'dir': 'v'}), (5, 8, {'dir': '^'}), (8, 9, {'dir': '>'}), (9, 8, {'dir': '<'}),
        (9, 6, {'dir': 'v'}), (6, 9, {'dir': '^'}), (6, 9, {'dir': '^'}), (6, 5, {'dir': '<'}),
        (5, 6, {'dir': '>'}), (4, 5, {'dir': '>'}), (5, 4, {'dir': '<'}), (4, 1, {'dir': 'v'}),
        (1, 4, {'dir': '^'}), (1, 2, {'dir': '>'}), (2, 1, {'dir': '<'}), (2, 5, {'dir': '^'}),
        (5, 2, {'dir': 'v'}), (2, 3, {'dir': '>'}), (3, 2, {'dir': '<'}), (2, 0, {'dir': 'v'}),
        (0, 2, {'dir': '^'}), (3, 6, {'dir': '^'}), (3, 'A', {'dir': 'v'}), ('A', 3, {'dir': '^'}),
        (0, 'A', {'dir': '>'}), ('A', 0, {'dir': '<'}), (6, 3, {'dir': 'v'})])

dir_pad_paths = dict(nx.all_pairs_shortest_path(dir_pad))
num_pad_paths = dict(nx.all_pairs_shortest_path(num_pad))

def get_num_pad_presses(current_location, goal):
    shortest_path = num_pad_paths[current_location][goal]
    presses = ''
    for i in range(1, len(shortest_path)):
        first_node = shortest_path[i - 1]
        second_node = shortest_path[i]
        presses += num_pad.edges[first_node, second_node]['dir']
    return presses + 'A'

def get_dir_pad_presses(current_location, goal):
    shortest_path = dir_pad_paths[current_location][goal]
    presses = ''
    for i in range(1, len(shortest_path)):
        first_node = shortest_path[i - 1]
        second_node = shortest_path[i]
        presses += dir_pad.edges[first_node, second_node]['dir']
    return presses + 'A'


"""print(f"From 9 to 0: {get_num_pad_presses(9, 0)}")
print(f"From 0 to 9: {get_num_pad_presses(0, 9)}")
print(f"From < to A: {get_dir_pad_presses('<', 'A')}")
print(f"From A to <: {get_dir_pad_presses('A', '<')}")
print(f"From A to A: {get_dir_pad_presses('A', 'A')}")"""

access_code = '029A'
current_position = 'A'
total_presses = ''
for i in range(0, len(access_code)):
    next_position = access_code[i]
    if next_position != 'A':
        next_position = int(next_position)
    total_presses += get_num_pad_presses(current_position, next_position)
    current_position = next_position

print(total_presses)