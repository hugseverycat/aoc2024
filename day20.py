from collections import defaultdict

with open('input/20.txt') as f:
    lines = [line.rstrip() for line in f]

track = defaultdict(int)
walls = dict()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for y, this_line in enumerate(lines):
    for x, this_char in enumerate(this_line):
        if this_char == 'S':
            start = (x, y)
            track[(x, y)] = None
        elif this_char == 'E':
            goal = (x, y)
            track[(x, y)] = None
        elif this_char == '#':
            walls[(x, y)] = None
        else:
            track[(x, y)] = None

cx, cy = start
path = [start]
step = 0
track[start] = step
while (cx, cy) != goal:
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if (nx, ny) in track and (nx, ny) not in path:
            path.append((nx, ny))
            step += 1
            track[(nx, ny)] = step
            cx += dx
            cy += dy
            break

# Note, len(path) overcounts by 1
cheat_dirs = [(0, -2), (1, -1), (2, 0), (1, 1), (0, 2), (-1, 1), (-2, 0), (-1, -1)]
good_cheats = 0
for px, py in path:
    current_distance = track[(px, py)]
    for dx, dy in cheat_dirs:
        nx, ny = px + dx, py + dy
        if (nx, ny) in track and track[(nx, ny)] - 2 > track[(px, py)]:
            gain = track[(nx, ny)] - 2 - track[(px, py)]
            if gain >= 100:
                good_cheats += 1

print(good_cheats)
