import re

test = False
if test:
    filename = 'input/sample.txt'
    area_width = 11
    area_height = 7
else:
    filename = 'input/14.txt'
    area_width = 101
    area_height = 103


with open(filename) as f:
    lines = [line.rstrip() for line in f]

robots = []
for this_line in lines:
    robot_nums = [int(x) for x in re.findall('-?\d+', this_line)]
    robots.append(robot_nums)


def get_quadrant(x: int, y: int):
    if x == area_width // 2 or y == area_height // 2:
        return None
    if x < area_width // 2 and y < area_height // 2:
        return 0
    if x > area_width // 2 and y < area_height // 2:
        return 1
    if x < area_width // 2 and y > area_height // 2:
        return 2
    if x > area_width // 2 and y > area_height // 2:
        return 3


def get_robot_position(bot: list, s: int):
    px, py = bot[0], bot[1]
    dx, dy = bot[2], bot[3]
    px = (px + dx * s) % area_width
    py = (py + dy * s) % area_height
    return px, py


safety_scores = []
for i in range(10000):
    quadrants = [0, 0, 0, 0]
    for this_robot in robots:
        bx, by = get_robot_position(this_robot, i)
        q = get_quadrant(bx, by)
        if q is not None:
            quadrants[q] += 1
    safety_score = 1
    for q in quadrants:
        safety_score *= q
    safety_scores.append(safety_score)
    if i == 100:
        print(f"Part 1: {safety_score}")

# Guess: the picture will have a minimum safety score because lots of robots will be grouped together
min_safety = safety_scores.index(min(safety_scores))

# Print the picture, for fun (and confirmation)
tree_picture = set()
for this_robot in robots:
    tree_picture.add(get_robot_position(this_robot, min_safety))
for this_y in range(area_height):
    print_line = ''
    for this_x in range(area_width):
        if (this_x, this_y) in tree_picture:
            print_line += '🟢'
        else:
            print_line += '⬜'
    print(print_line)

print(f"Part 2: {min_safety}")
