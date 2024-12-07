with open('input/06.txt') as f:
    lines = [line.rstrip() for line in f]

obs_set = set()  # (x, y) coordinates of each obstruction
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
            obs_set.add((x, y))
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

    # If we find an obstruction, turn
    if (curr_x + dx, curr_y + dy) in obs_set:
        direction_index = (direction_index + 1) % 4
    else:
        # Otherwise, continue in the same direction
        curr_x += dx
        curr_y += dy
print(f"Part 1: {len(visited)}")

# Now lets check what happens if we place an obstruction on every location we've visited
for potential_obs in visited:
    # Create a temporary obstruction set with the original obstructions + this potential one
    temp_obstructions = obs_set.union({potential_obs})

    # Reset our starting location and direction
    curr_x, curr_y = start_x, start_y
    direction_index = 0

    # A set to keep track of where we turn, and what direction we're coming from
    # If we hit this turn coming from the same direction, we've found a loop
    temp_visited = set()

    # Now we will travel the path with this new obstruction
    while curr_x in range(0, x_bound) and curr_y in range(0, y_bound):
        # Get our current direction
        dx, dy = direction_set[direction_index]

        # Try to move or turn like we did in part 1
        if (curr_x + dx, curr_y + dy) in temp_obstructions:
            # We found a turn, let's check to see if we've made this same turn before
            if (curr_x, curr_y, dx, dy) in temp_visited:
                # We've made this exact turn before so we've found a loop. Stop checking.
                obstructions += 1
                break
            # This is a new turn, add it to the set and make the turn
            temp_visited.add((curr_x, curr_y, dx, dy))
            direction_index = (direction_index + 1) % 4
        else:
            curr_x += dx
            curr_y += dy

print(f"Part 2: {obstructions}")
