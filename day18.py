from collections import deque, defaultdict
test = False
if test:
    filename = 'input/sample.txt'
    x_bound = y_bound = 6
    time = 21
else:
    filename = 'input/18.txt'
    x_bound = y_bound = 70
    time = 1024


def print_map(b_map: defaultdict, b_path: list = None):
    if b_path is None:
        b_path = []
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


def find_path(bt: int, byte_list: list):
    # Use BFS to find a path
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0, 0)
    goal = (x_bound, y_bound)
    b_map = defaultdict(str)
    # Populate the map with all the falling bytes by time t
    for t in range(bt):
        b_map[byte_list[t]] = '#'

    # Queue to check the adjacent squares. This is a deque because we will be removing items from the front
    move_queue = deque([start])
    # If you step from square A to square B, then paths[B] = A. Helps reconstruct the path and prevent backtracking
    paths = dict()
    paths[start] = None
    while move_queue:
        # Remove the oldest item from the queue. Once the queue is empty, this will stop looking
        current_loc = move_queue.popleft()
        if current_loc == goal:
            break

        cx, cy = current_loc
        # For each neighbor, we'll check if it's in bounds first.
        # Then if we haven't been there already (in the paths dict) and it's not corrupted, add it to the queue
        for this_dir in directions:
            dx, dy = this_dir
            nx, ny = cx + dx, cy + dy
            if nx in range(0, x_bound + 1) and ny in range(0, y_bound + 1):
                if (nx, ny) not in paths and b_map[(nx, ny)] != '#':
                    move_queue.append((cx + dx, cy + dy))
                    paths[(cx + dx, cy + dy)] = current_loc

    # Now we will start at the goal and walk backwards along the paths dict to find the actual path
    current_loc = goal
    best_path = []
    while current_loc != start:
        best_path.append(current_loc)
        try:
            current_loc = paths[current_loc]
        except KeyError:
            # If we never reached the goal, then paths dict will not have an entry for the goal tuple and will
            # give a KeyError. Return an empty list
            return []
    # If we did reach the goal, return the path
    return best_path


with open(filename) as f:
    lines = [line.rstrip() for line in f]

falling_bytes = []
for this_line in lines:
    bx, by = [int(x) for x in this_line.split(',')]
    falling_bytes.append((bx, by))

print(f"Part 1: {len(find_path(time, falling_bytes))}")

# Binary search to find the first byte that fails to find a path
low = time  # We know that 1024 gives a result so that will be our low bound
high = len(lines)
mid = low + (high - low) // 2
while True:
    path_length = len(find_path(mid, falling_bytes))
    if path_length > 0:  # too low
        low = mid
        mid = low + (high - low) // 2
    else:  # too high
        high = mid
        mid = low + (high - low) // 2
    if low == high or mid == low or mid == high:  # I'm not sure which of these conditions is correct so I check all
        break

bx, by = falling_bytes[mid]
print(f"Part 2: {bx},{by}")
