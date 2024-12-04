with open('input/04.txt') as f:
    lines = [line.rstrip() for line in f]

# Using sets so that I can quickly look up a letter without having to worry
# about indices being out of range
x_locations = set()
m_locations = set()
a_locations = set()
s_locations = set()

for y, this_row in enumerate(lines):
    for x, this_char in enumerate(this_row):
        if this_char == 'X':
            x_locations.add((x, y))
        elif this_char == 'M':
            m_locations.add((x, y))
        elif this_char == 'A':
            a_locations.add((x, y))
        elif this_char == 'S':
            s_locations.add((x, y))

# Part 1
xmas_found = 0
for this_x in x_locations:
    x, y = this_x
    # Check each adjacent square for an M. If one is found, keep looking in the same direction
    # for an A, then an S.
    for this_step in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        step_x, step_y = this_step
        if (x + step_x, y + step_y) in m_locations:
            if (x + step_x * 2, y + step_y * 2) in a_locations:
                if (x + step_x * 3, y + step_y * 3) in s_locations:
                    xmas_found += 1
print(f"Part 1: {xmas_found}")

# Part 2
xmas_found = 0
for this_a in a_locations:
    x, y = this_a
    # Check each corner for an M, If one is found, check the opposite corner for an S.
    # If the S is found, then check for an appropriate M and S on the other diagonal.
    for this_step in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        step_x, step_y = this_step
        if (x + step_x, y + step_y) in m_locations:
            if (x - step_x, y - step_y) in s_locations:
                if (x + step_x, y - step_y) in m_locations:  # Same X, mirrored Y
                    if (x - step_x, y + step_y) in s_locations:  # Same Y, mirrored X
                        xmas_found += 1
                        break  # Stop checking in order to avoid counting each X-MAS twice
                elif (x - step_x, y + step_y) in m_locations:  # Same Y, mirrored X
                    if (x + step_x, y - step_y) in s_locations:  # Same X, mirrored Y
                        xmas_found += 1
                        break
print(f"Part 2: {xmas_found}")
