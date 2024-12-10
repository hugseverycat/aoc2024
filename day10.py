from collections import defaultdict
with open('input/10.txt') as f:
    lines = [line.rstrip() for line in f]

top_map = defaultdict(int)
trailheads = set()
for y, this_line in enumerate(lines):
    for x, this_char in enumerate(this_line):
        if this_char == '.':
            top_map[(x, y)] = -1
        else:
            top_map[(x, y)] = int(this_char)
        if this_char == '0':
            trailheads.add((x, y))


def blah(h: int, coords: tuple, found: set, t_map: dict) -> set:
    t_score = 0
    # If I'm a 9, add it to the found set and return
    if h == 9:
        found.add(coords)
        return found
    # If I'm not a 9, look for neighbors increasing by 1
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cx, cy = coords
    for this_n in neighbors:
        nx, ny = this_n
        if t_map[(cx+nx, cy+ny)] == h + 1:
            found.union(blah(h+1, (cx+nx, cy+ny), found, t_map))
    return found


total_score = 0
for this_trailhead in trailheads:
    #print(f"Checking trailhead at {this_trailhead}")
    this_score = len(blah(0, this_trailhead, set(), top_map))
    #print(f"Trailhead score: {this_score}")
    total_score += this_score
    #print()

print(total_score)