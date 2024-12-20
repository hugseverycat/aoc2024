from collections import deque
import heapq

with open('input/16.txt') as path_score:
    lines = [line.rstrip() for line in path_score]

x_bound = len(lines[0])
y_bound = len(lines)
maze = dict()
solution_paths = []

for y, this_line in enumerate(lines):
    for x, this_char in enumerate(this_line):
        if this_char == 'S':
            start = (x, y)
            maze[(x, y)] = '.'
        elif this_char == 'E':
            goal = (x, y)
            maze[(x, y)] = '.'
        else:
            maze[(x, y)] = this_char


def draw_path(maze_map: dict, maze_path: list):
    print()
    for py in range(0, y_bound):
        new_line = ''
        for px in range(0, x_bound):
            if (px, py) == start:
                new_line += '⭐'
            elif (px, py) == goal:
                new_line += '⭐'
            elif (px, py) in maze_path :
                new_line += '👠'
            elif maze_map[(px, py)] == '#':
                new_line += '🪨'
            else:
                new_line += '◼️'
        print(new_line)
    print()


def find_path(maze_map: dict, s: tuple, g: tuple):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction = 0
    score = 0
    queue = [(score, s, direction)]
    heapq.heapify(queue)
    visited_from = {(s, direction): None}
    scores = {(s, direction): 0}
    final_score = 0
    while queue:
        current_score, (cx, cy), current_d = heapq.heappop(queue)
        if (cx, cy) == g:
            final_score = current_score
            break
        for nd, (dx, dy) in enumerate(d):
            nx, ny = cx + dx, cy + dy
            if maze_map[(nx, ny)] != '#':
                if nd == current_d:  # If we're going in the same direction we're facing
                    new_score = current_score + 1
                elif nd == (current_d + 1) % 4:  # We are turning clockwise
                    new_score = current_score + 1001
                elif nd == (current_d - 1) % 4:  # We are turning counter-clockwise
                    new_score = current_score + 1001
                else:  # We are turning around
                    new_score = current_score + 2001
                if ((nx, ny), nd) not in visited_from or new_score < scores[((nx, ny), nd)]:
                    try:
                        if new_score < scores[((nx, ny), nd)]:
                            pass
                    except KeyError:
                        pass
                    visited_from[((nx, ny), nd)] = ((cx, cy), current_d)
                    scores[((nx, ny), nd)] = new_score
                    heapq.heappush(queue, (new_score, (nx, ny), nd))
            else:
                pass

    next_coord, next_dir = visited_from[(goal, current_d)]
    path = [next_coord]
    while next_coord != start:
        next_coord, next_dir = visited_from[(next_coord, next_dir)]
        path.append(next_coord)
    return [path, final_score]


optimal_path, path_score = find_path(maze, start, goal)
print(f"Part 1: {path_score}")
