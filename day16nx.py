import networkx as nx

with open('input/16.txt') as f:
    lines = [line.rstrip() for line in f]

maze_map = dict()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d_index = 0
G = nx.Graph()
for y, this_line in enumerate(lines):
    for x, this_char in enumerate(this_line):
        if this_char == 'S':
            start = (x, y, 0)
        elif this_char == 'E':
            end = (x, y)
        maze_map[(x, y)] = this_char

for this_location in maze_map:
    if maze_map[this_location] != '#':
        cx, cy = this_location
        for facing_d in range(4):  # Direction I am facing
            for moving_d in range(4):  #Direction I will travel
                ndx, ndy = directions[moving_d]
                ex, ey = end
                if (cx + ndx, cy + ndy) == (ex, ey):
                    next_node = (ex, ey)
                else:
                    next_node = (cx + ndx, cy + ndy, moving_d)
                if maze_map[(cx + ndx, cy + ndy)] != '#':
                    if facing_d == moving_d:
                        # G.add_weighted_edges_from([((0, 0, 1), (0, 0, 2), 5)])
                        G.add_weighted_edges_from([((cx, cy, facing_d), next_node, 1)])
                    elif facing_d == (moving_d + 1) % 4 or facing_d == (moving_d - 1) % 4:
                        G.add_weighted_edges_from([((cx, cy, facing_d), next_node, 1001)])
                    else:
                        G.add_weighted_edges_from([((cx, cy, facing_d), next_node, 2001)])

shortest = nx.dijkstra_path_length(G, start, end)
print(shortest)
