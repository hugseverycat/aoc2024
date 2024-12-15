with open('input/15.txt') as f:
    lines = [line.rstrip() for line in f]

x_bound = len(lines[0])

switch = False
warehouse_map = dict()
m = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1)
}


moves = []
robot = tuple()
for y, this_line in enumerate(lines):
    if this_line == '':
        y_bound = y
        switch = True
    if not switch:
        for x, this_char in enumerate(this_line):
            if this_char == '@':
                robot = (x, y)
                warehouse_map[(x, y)] = '.'
            else:
                warehouse_map[(x, y)] = this_char
    else:
        for this_char in this_line:
            moves.append(this_char)


def print_map(w_map: dict):
    print()
    for py in range(y_bound):
        print_line = ''
        for px in range(x_bound):
            c = w_map[(px, py)]
            if c == '#':
                c = '🪨'
            elif c == '.':
                c = '⬛'
            elif c == 'O':
                c = '📦'
            elif c == '@':
                c = '🤖'
            print_line += c
        print(print_line)
    print()


i = 0
for move in moves:
    dx, dy = m[move]
    movers = dict()  # Things that will move if we find room
    move_possible = True
    x, y = robot
    i += 1
    while True:
        if warehouse_map[(x + dx, y + dy)] == '.':
            # We found an empty space. All the things that need to move can move.
            movers[(x + dx, y + dy)] = warehouse_map[(x, y)]
            break
        elif warehouse_map[(x + dx, y + dy)] == 'O':
            # We found a box. Let's try to move this box, too.
            movers[(x + dx, y + dy)] = warehouse_map[(x, y)]
            x += dx
            y += dy
        else:  # We found a wall and nothing can move
            move_possible = False
            break
    if move_possible:
        for this_mover in movers:
            warehouse_map[this_mover] = movers[this_mover]
        warehouse_map[robot] = '.'
        rx, ry = robot
        robot = (rx + dx, ry + dy)
        warehouse_map[robot] = '@'

print_map(warehouse_map)
gps_sum = 0
for coord in warehouse_map:
    cx, cy = coord
    if warehouse_map[coord] == 'O':
        gps_sum += cx + 100 * cy
print(f"Part 1: {gps_sum}")
