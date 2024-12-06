with open('input/06.txt') as f:
    lines = [line.rstrip() for line in f]

obstacles = set()
x_bound = 0
y_bound = 0
curr_x, curr_y = None, None
for y, line in enumerate(lines):
    if not x_bound:
        x_bound = len(line)
    for x, this_char in enumerate(line):
        if this_char == '#':
            obstacles.add((x, y))
        elif this_char == '^':
            curr_x, curr_y = x, y
    y_bound += 1

direction_set = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction_index = 0
visited = set()
positions = set()
obstructions = 0

while curr_x in range(0, x_bound) and curr_y in range(0, y_bound):
    visited.add((curr_x, curr_y))
    dx, dy = direction_set[direction_index]
    positions.add((curr_x, curr_y, dx, dy))
    if (curr_x + dx, curr_y + dy) in obstacles:
        direction_index = (direction_index + 1) % 4
    else:
        curr_x += dx
        curr_y += dy
print(f"Part 1: {len(visited)}")
