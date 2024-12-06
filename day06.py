with open('input/06.txt') as f:
    lines = [line.rstrip() for line in f]

obstacles = set()  # (x, y) coordinates of each obstacle
visited = set()  # (x, y) coordinates of each location visited for part 1
x_bound = 0
y_bound = 0
start_x, start_y = None, None
direction_set = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # When we turn to the right, increase the index by 1 then mod 4
direction_index = 0
obstructions = 0  # Counter for part 2

for y, line in enumerate(lines):
    if not x_bound:
        x_bound = len(line)
    for x, this_char in enumerate(line):
        if this_char == '#':
            obstacles.add((x, y))
        elif this_char == '^':
            start_x, start_y = x, y
    y_bound += 1

curr_x, curr_y = start_x, start_y

# Part 1
while curr_x in range(0, x_bound) and curr_y in range(0, y_bound):
    # Get the current direction
    dx, dy = direction_set[direction_index]

    # Add the current position to visited set (for part 1)
    visited.add((curr_x, curr_y))

    # If we find an obstacle, turn
    if (curr_x + dx, curr_y + dy) in obstacles:
        direction_index = (direction_index + 1) % 4
    else:
        # Otherwise, continue in the same direction
        curr_x += dx
        curr_y += dy
print(f"Part 1: {len(visited)}")

# Now lets check what happens if we place an obstacle on every location we've visited
for potential_obs in visited:
    # Pull the x, y of this potential obstacle
    ox, oy = potential_obs

    # Create a temporary obstacle set with the original obstacles + this potential one
    temp_obstructions = obstacles.union({(ox, oy)})

    # Reset our starting location and direction
    curr_x, curr_y = start_x, start_y
    direction_index = 0

    # A new set of visited locations and directions for this theoretical
    # If we ever revisit a location going in the same direction we were before, we know we have a loop
    temp_visited = set()

    # Now we will travel the path with this new obstacle
    while curr_x in range(0, x_bound) and curr_y in range(0, y_bound):
        # Get our current direction
        dx, dy = direction_set[direction_index]
        # Check if we've been here before while going the same direction
        if (curr_x, curr_y, dx, dy) in temp_visited:
            # If we have, the obstruction we are testing creates a loop, no need to go further
            obstructions += 1
            break

        # If not, add it to the temporary visited set
        temp_visited.add((curr_x, curr_y, dx, dy))

        # Move or turn like we did in part 1
        if (curr_x + dx, curr_y + dy) in temp_obstructions:
            direction_index = (direction_index + 1) % 4
        else:
            curr_x += dx
            curr_y += dy

print(f"Part 2: {obstructions}")

