with open('input/15.txt') as f:
    lines = [line.rstrip() for line in f]

x_bound = len(lines[0]) * 2
warehouse_map = dict()
m = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1)
}
moves = []
robot = tuple()
switch = False
for y, this_line in enumerate(lines):
    if this_line == '':
        y_bound = y
        switch = True
    if not switch:
        for x, this_char in enumerate(this_line):
            if this_char == '@':
                robot = (x * 2, y)
                warehouse_map[(x * 2, y)] = '@'
                warehouse_map[(x * 2 + 1, y)] = '.'
            elif this_char == 'O':
                warehouse_map[(x * 2, y)] = '['
                warehouse_map[(x * 2 + 1, y)] = ']'
            else:
                warehouse_map[(x * 2, y)] = this_char
                warehouse_map[(x * 2 + 1, y)] = this_char
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
            elif c in 'O[':
                c = '📦'
            elif c == ']':
                c = '🎁'
            elif c == '@':
                c = '🤖'
            print_line += c
        print(print_line)
    print()


for move in moves:
    dx, dy = m[move]  # Get the direction we're moving in
    move_possible = True  # If we hit a wall, this will turn False
    movers = {robot: warehouse_map[robot]}  # Things that will move if move_possible is still True at the end
    rx, ry = robot
    to_check = [(rx, ry)]
    # Since we could potentially be moving lots of stuff at once, we'll keep a queue of things we're going to move
    # that we need to check we have room for. When moving horizontally, we'll only add the far side of a box to this
    # queue, since that's the side that could potentially hit a wall. Whe moving vertically, we'll add both sides of
    # each box to the queue since either side could hit a wall (or a new box).
    while to_check:
        cx, cy = to_check.pop()  # My actual location
        mx, my = cx + dx, cy + dy  # The location I want to move to
        if move == '<':
            if warehouse_map[(mx, my)] == ']':
                # We are moving left and we found the right side of the box. Add it and the left side to the movers
                # dictionary and then add the left side of the box to the queue to make sure it has room to move
                movers[(mx, my)] = warehouse_map[(mx, my)]
                movers[(mx - 1, my)] = warehouse_map[(mx - 1, my)]
                to_check.append((mx - 1, my))
            elif warehouse_map[(mx, my)] == '#':
                # We found a wall. No move is possible. Stop checking.
                move_possible = False
                break
        elif move == '>':
            if warehouse_map[(mx, my)] == '[':
                # We are moving right and we found the left side of the box. Add it and the right side to the movers
                # dictionary and then add the right side of the box to the queue to make sure it has room to move
                movers[(mx, my)] = warehouse_map[(mx, my)]
                movers[(mx + 1, my)] = warehouse_map[(mx + 1, my)]
                to_check.append((mx + 1, my))
            elif warehouse_map[(mx, my)] == '#':
                # We found a wall. No move is possible. Stop checking.
                move_possible = False
                break
        elif move in '^v':
            if warehouse_map[(mx, my)] == '[':
                # We are moving vertically and we found the left side of a box. Add it and the right side to the
                # movers dictionary and then add both sides to the queue to make sure it has room to move
                movers[(mx, my)] = warehouse_map[(mx, my)]
                movers[(mx + 1, my)] = warehouse_map[(mx + 1, my)]
                to_check.extend([(mx, my), (mx + 1, my)])
            elif warehouse_map[(mx, my)] == '#':
                # We found a wall. No move is possible. Stop checking.
                move_possible = False
                break
            elif warehouse_map[(mx, my)] == ']':
                # We are moving vertically and we found the right side of a box. Add it and the left side to the movers
                # dictionary and then add both sides tot he queue to make sure it has room to move
                movers[(mx, my)] = warehouse_map[(mx, my)]
                movers[(mx - 1, my)] = warehouse_map[(mx - 1, my)]
                to_check.extend([(mx, my), (mx - 1, my)])

    if move_possible:
        # Set all the original locations to '.' in the warehouse_map
        for this_loc in movers:
            warehouse_map[this_loc] = '.'
        # Move everyone to their new location
        for this_mover in movers:
            mx, my = this_mover
            warehouse_map[(mx + dx, my + dy)] = movers[this_mover]
        robot = (rx + dx, ry + dy)
        warehouse_map[robot] = '@'

gps_sum = 0
for coord in warehouse_map:
    cx, cy = coord
    if warehouse_map[coord] == '[':
        gps_sum += cx + 100 * cy
print_map(warehouse_map)
print(f"Part 2: {gps_sum}")
