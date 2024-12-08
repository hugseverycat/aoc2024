from collections import defaultdict

with open('input/08.txt') as f:
    lines = [line.rstrip() for line in f]

y_bound = len(lines)
x_bound = 0
antenna_types = defaultdict(list)
for y, this_line in enumerate(lines):
    if not x_bound:
        x_bound = len(this_line)
    for x, this_char in enumerate(this_line):
        if this_char != '.':
            # Keeping track of the (x, y) location of each type of antenna
            antenna_types[this_char].append((x, y))

antinodes = set()  # Using a set so duplicates are automatically removed
for this_type in antenna_types:
    type_len = len(antenna_types[this_type])

    # Compare each antenna of a type to each antenna after it in the list
    for a1 in range(0, type_len - 1):
        first = antenna_types[this_type][a1]
        for a2 in range(a1 + 1, type_len):
            second = antenna_types[this_type][a2]
            # Add both antennas to the antinode set.
            antinodes.add(first)
            antinodes.add(second)
            fx, fy = first
            sx, sy = second
            # Calculate the x and y distance between the first and second antenna
            dx = fx - sx
            dy = fy - sy
            # Create antinodes in the positive direction from the first antenna
            while fx + dx in range(0, x_bound) and fy + dy in range(0, y_bound):
                antinodes.add((fx + dx, fy + dy))
                fx += dx
                fy += dy
            # Create antinodes in the negative direction from the second antenna
            while sx - dx in range(0, x_bound) and sy - dy in range(0, y_bound):
                antinodes.add((sx - dx, sy - dy))
                sx -= dx
                sy -= dy

print(f"Part 2: {len(antinodes)}")
