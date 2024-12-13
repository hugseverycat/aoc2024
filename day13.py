from collections import namedtuple
import re

with open('input/13.txt') as f:
    lines = [line.rstrip() for line in f]

Claw = namedtuple('Claw', ['button_a', 'button_b', 'prize'])
claws = []
a_cost = 3
b_cost = 1

for i in range(0, len(lines)//4 + 1):
    a = tuple([int(x) for x in re.findall('\d+', lines[i*4])])
    b = tuple([int(x) for x in re.findall('\d+', lines[i*4+1])])
    p = tuple([int(x) for x in re.findall('\d+', lines[i*4+2])])
    claws.append(Claw(a, b, p))

total_cost = 0
for n, this_claw in enumerate(claws):
    cost = None
    target_x, target_y = this_claw.prize
    a_x, a_y = this_claw.button_a

    for b_count in range(0, 100):
        # Where would we be if we pressed B b_count times?
        b_x, b_y = (b_count * this_claw.button_b[0], b_count * this_claw.button_b[1])

        # If we haven't gone too far, let's continue
        if b_x < target_x and b_y < target_y:
            # Find how far we have left to go in the x direction and the y direction
            # Then see if it is even possible for us to get there by pressing A
            # For example, if we have to go 100 steps in x, but a moves us 3 steps, we can't get there
            # So we need to take the x distance remaining and get the mod of the a direction and see if it is zero
            if (target_x - b_x) % a_x == 0 and (target_y - b_y) % a_y == 0:
                # Now we have to make sure that the number of x and y steps for A match each other
                a_x_steps = (target_x - b_x) // a_x
                a_y_steps = (target_y - b_y) // a_y
                if a_x_steps == a_y_steps:
                    temp_cost = a_cost * ((target_x - b_x) // a_x) + (b_count) * b_cost
                    if cost is None:
                        # If this is the first time we've found a match, calculate and save the cost
                        # Cost = b_count * b_cost + distance // a_x * a_cost
                        cost = temp_cost
                    else:
                        if temp_cost < cost:
                            cost = temp_cost
    if cost is not None:
        total_cost += cost

print(f"Part 1: {total_cost}")
# Wrong answers
# Part 1: 59690 (too high)
# Part 1: 59962 (too high)