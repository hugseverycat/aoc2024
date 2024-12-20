import re

with open('input/19.txt') as f:
    lines = [line.rstrip() for line in f]

towels = []
patterns = []
switch = False
for this_line in lines:
    if switch:
        patterns.append(this_line)
    elif this_line == '':
        switch = True
    else:
        towels = this_line.split(', ')

def find_pattern(p_to_find, p_so_far=''):
    if p_to_find == p_so_far:
        return True
    found = False
    for this_towel in towels:
        if found:
            return True
        new_partial_pattern = p_so_far + this_towel
        if re.search('^' + new_partial_pattern, p_to_find):
            found = find_pattern(p_to_find, new_partial_pattern)
    return False

def find_pattern_part2(p_to_find, p_so_far=''):
    if p_to_find == p_so_far:
        return 1
    found_counter = 0
    for this_towel in towels:
        new_partial_pattern = p_so_far + this_towel
        if re.search('^' + new_partial_pattern, p_to_find):
            found_counter += find_pattern_part2(p_to_find, new_partial_pattern)
    return found_counter

part1 = False
if part1:
    counter = 0
    for this_pattern in patterns:
        if find_pattern(this_pattern):
            counter += 1

else:
    counter = 0
    for this_pattern in patterns:
        counter += find_pattern_part2(this_pattern)

print(counter)