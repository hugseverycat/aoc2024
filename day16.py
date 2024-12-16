from collections import deque
import heapq

with open('input/sample.txt') as f:
    lines = [line.rstrip() for line in f]

x_bound = len(lines[0])
y_bound = len(lines)
maze = dict()
states = dict()
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direction = 0
solution_paths = []
final_score = 0
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


"""
def dijkstra_search(graph: WeightedGraph, start: Location, goal: Location):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: dict[Location, Optional[Location]] = {}
    cost_so_far: dict[Location, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current: Location = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far
"""



score = 0
queue = [(score, start, direction)]
heapq.heapify(queue)
visited_from = dict()
visited_from[(start, direction)] = None
scores = dict()
scores[(start, direction)] = 0
#print(f"Starting from {start}")
final_score = 0
while queue:
    current_score, (cx, cy), current_d = heapq.heappop(queue)
    #print()
    #print(f"  Visiting {(cx, cy)} in direction {current_d}")
    if (cx, cy) == goal:
        final_score = current_score
        break
    for nd, (dx, dy) in enumerate(d):
        #print(f"    Looking in direction {current_d}: {dx, dy}")
        nx, ny = cx + dx, cy + dy
        if maze[(nx, ny)] != '#':
            #print(f"    Considering {(nx, ny)} in direction {nd}")
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
                        #print(f"    We've been here before, but old score {scores[((nx, ny), nd)]} > new score {new_score}")
                        pass
                except KeyError:
                    pass
                #print(f"    Adding {(nx, ny)} in direction {nd} to the queue with score {new_score}")
                visited_from[((nx, ny), nd)] = ((cx, cy), current_d)  # Should this be di or current_direction
                scores[((nx, ny), nd)] = new_score
                heapq.heappush(queue, (new_score, (nx, ny), nd))
        else:
            #print(f"    {(nx, ny)} is a wall")
            pass

# Wrong answers
# 107508 too high
next_coord, next_dir = visited_from[(goal, current_d)]
path = [next_coord]
while next_coord != start:
    next_coord, next_dir = visited_from[(next_coord, next_dir)]
    path.append(next_coord)

draw_path(maze, path)
print(final_score)

new_queue = deque([(goal, current_d)])
print(len(new_queue))
print(new_queue)
while new_queue:
    (cx, cy), cd = new_queue.popleft()