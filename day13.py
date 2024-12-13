from collections import namedtuple
import re

with open('input/13.txt') as f:
    lines = [line.rstrip() for line in f]

Claw = namedtuple('Claw', ['button_a', 'button_b', 'prize'])
claws = []

for i in range(0, len(lines)//4 + 1):
    a = tuple([int(x) for x in re.findall('\d+', lines[i*4])])
    b = tuple([int(x) for x in re.findall('\d+', lines[i*4+1])])
    p = tuple([int(x) for x in re.findall('\d+', lines[i*4+2])])
    claws.append(Claw(a, b, p))


def find_solution(test_claw: Claw, incr=0):
    ax, ay = test_claw.button_a
    bx, by = test_claw.button_b
    px, py = test_claw.prize
    px += incr  # For part 2
    py += incr
    solution_a, solution_b = None, None  # If the solution isn't an integer, it will stay "None"

    # This nasty equation was worked out using algebra. If you're curious, see my comment on reddit here:
    # https://www.reddit.com/r/adventofcode/comments/1hd7irq/comment/m1xtxxc/
    if (bx * py - by * px) / (bx * ay - by * ax) == (bx * py - by * px) // (bx * ay - by * ax):
        # If statement compares regular division with integer division to make sure solution is an integer
        # If it's an integer, store it in solution_a
        solution_a = (bx * py - by * px) // (bx * ay - by * ax)
        if (py - solution_a * ay) / by == (py - solution_a * ay) // by:
            # We also want solution_b to be an integer
            solution_b = (py - solution_a * ay) // by
    if solution_a is not None and solution_b is not None:
        # If both solutions are integers, return the cost
        return solution_a * 3 + solution_b
    else:
        return 0


total_cost_1 = 0
total_cost_2 = 0
increase = 10000000000000

for this_claw in claws:
    total_cost_1 += find_solution(this_claw)
    total_cost_2 += find_solution(this_claw, increase)

print(f"Part 1: {total_cost_1}")
print(f"Part 2: {total_cost_2}")
