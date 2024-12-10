from collections import defaultdict
with open('input/10.txt') as f:
    lines = [line.rstrip() for line in f]

top_map = defaultdict(int)
trailheads = set()
for y, this_line in enumerate(lines):
    for x, this_char in enumerate(this_line):
        top_map[(x, y)] = int(this_char)
        if this_char == '0':
            trailheads.add((x, y))


def part_1_find_trails(h: int, coords: tuple, found: set, t_map: dict) -> set:
    """
    A recursive function to find trails that increase by 1 every step and end at a location with height 9.
    Only unique locations of height 9 are returned.

    :param h: The height of the coordinate we are at right now
    :param coords: The (x, y) coordinate of our current location
    :param found: A set of coordinates for height-9 locations we've already found for this trailhead
    :param t_map: The topographical map. Key:(x, y) coordinate. Value: height
    :return: The set of all height-9 locations this trailhead leads to
    """
    # If I'm a 9, we've found a path! Add it to the found set and return the set
    if h == 9:
        found.add(coords)
        return found
    # If I'm not a 9, look for neighbors increasing by 1
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cx, cy = coords
    for this_n in neighbors:
        nx, ny = this_n
        # If I find a neighbor that increases by 1, recursively call the same function for that neighbor
        if t_map[(cx+nx, cy+ny)] == h + 1:
            found.union(part_1_find_trails(h + 1, (cx+nx, cy+ny), found, t_map))
    # If this was a dead end, the found set will not have changed. At the end of all the recursion, the found set will
    # contain all the unique 9s we reached, and we can just count its size.
    return found


def part_2_find_trails(h: int, coords: tuple, t_map: dict) -> int:
    """
    A recursive function to find trails that increase by 1 step and end at a location with height 9.
    All unique trails are counted, even if they end at the same location with height 9.

    :param h: The height of the coordinate we are at right now
    :param coords: The (x, y) coordinate of our current location
    :param t_map: The topographical map. Key:(x, y) coordinate. Value: height
    :return: The number of unique paths to any location of height 9 starting at this trailhead
    """
    t_score = 0
    # If I'm a 9, we've found a trail! Return 1
    if h == 9:
        return 1
    # If I'm not a 9, look for neighbors increasing by 1
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cx, cy = coords
    for this_n in neighbors:
        nx, ny = this_n
        # If I find a neighbor that increases by 1, recursively call the same function for that neighbor
        if t_map[(cx+nx, cy+ny)] == h + 1:
            t_score += part_2_find_trails(h+1, (cx+nx, cy+ny), t_map)
    # If this was a dead end, t_score will be zero. At the end of all the recursion, this will be a count of all
    # unique paths that ended at 9.
    return t_score


part_1_score = 0
part_2_score = 0
for this_trailhead in trailheads:
    part_1_score += len(part_1_find_trails(0, this_trailhead, set(), top_map))
    part_2_score += part_2_find_trails(0, this_trailhead, top_map)

print(f"Part 1: {part_1_score}")
print(f"Part 2: {part_2_score}")
