from collections import defaultdict

with open('input/08.txt') as f:
    lines = [line.rstrip() for line in f]

antenna_map = dict()
antenna_types = defaultdict(list)
for y, this_line in enumerate(lines):
    for x, this_char in enumerate(this_line):
        antenna_map[(x, y)] = this_char
        if this_char != '.':
            antenna_types[this_char].append((x, y))

antinodes = set()
for this_type in antenna_types:
    type_len = len(antenna_types[this_type])

    for a1 in range(0, type_len - 1):
        first = antenna_types[this_type][a1]
        for a2 in range(a1 + 1, type_len):
            second = antenna_types[this_type][a2]
            dx = first[0] - second[0]
            dy = first[1] - second[1]
            antinode1 = (first[0] + dx, first[1] + dy)
            antinode2 = (second[0] - dx, second[1] - dy)
            if antinode1 in antenna_map:
                antinodes.add(antinode1)
            if antinode2 in antenna_map:
                antinodes.add(antinode2)

print(len(antinodes))
