from collections import deque, defaultdict
test = False
if test:
    filename = 'input/sample.txt'
    x_bound = y_bound = 6
    time = 21
else:
    filename = 'input/18.txt'
    x_bound = y_bound = 70
    time = 2934

def print_map(b_map: defaultdict, b_path: list = []):
    print()
    for py in range(y_bound + 1):
        print_line = ''
        for px in range(x_bound + 1):
            if (px, py) in b_path:
                print_line += '👠'
            elif b_map[(px, py)] == '#':
                print_line += '🤖'
            else:
                print_line += '◼️'
        print(print_line)
    print()

with open(filename) as f:
    lines = [line.rstrip() for line in f]

falling_bytes = []
byte_map = defaultdict(str)
for this_line in lines:
    bx, by = [int(x) for x in this_line.split(',')]
    falling_bytes.append((bx, by))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start = (0, 0)
goal = (x_bound, y_bound)
for t in range(time):
    byte_map[falling_bytes[t]] = '#'

move_queue = deque([start])
paths = dict()
paths[start] = None
i = 0
while move_queue:
    current_loc = move_queue.popleft()
    if current_loc == goal:
        break

    cx, cy = current_loc
    for this_dir in directions:
        dx, dy = this_dir
        nx, ny = cx + dx, cy + dy
        if nx in range(0, x_bound+1) and ny in range(0, y_bound+1):
            if (nx, ny) not in paths and byte_map[(nx, ny)] != '#':
                move_queue.append((cx + dx, cy + dy))
                paths[(cx + dx, cy + dy)] = current_loc

current_loc = goal
best_path = []
while current_loc != start:
    best_path.append(current_loc)
    try:
        current_loc = paths[current_loc]
    except:
        bx, by = falling_bytes[time - 1]
        print(f"Part 2: {bx},{by}")
        break

# Wrong answers
# 1510 (too high)
# 60,49