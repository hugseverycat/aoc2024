from collections import defaultdict

with open('input/05.txt') as f:
    lines = [line.rstrip() for line in f]

pairs = defaultdict(list)
updates = []
next_section = False
# Going to import the before|after rules as a dictionary. The key is the "before" number
# and the value will be a list of all numbers that must go "after" that number. For example,
# 1|2 and 1|3 will result in a dictionary entry 1: [2, 3]

# After detecting a blank line, we'll collect each line of updates and store them as lists in
# the updates list.
for line in lines:
    if next_section:
        updates.append([int(x) for x in line.split(',')])
    elif line == "":
        next_section = True
    else:
        first, second = [int(x) for x in line.split('|')]
        pairs[first].append(second)

middle_sum_p1 = 0
middle_sum_p2 = 0
# Observation of data: If a page is supposed to be before another page, it will ALWAYS have a rule for it. None of the
# rules are "indirect". So for example, if [a, b, c] is in order, then there is a rule a|b and a|c, and a rule b|c.
# This means you can count how many rules there are relating to the other pages in the update. So the count here would
# be [2, 1, 0]. If the update is in order, the number of rules will be in decreasing order.
for this_update in updates:
    before_list = []
    for page in this_update:
        before_count = 0
        for before in pairs[page]:
            if before in this_update:
                before_count += 1
        before_list.append(before_count)
    if before_list == sorted(before_list, reverse=True):
        middle_sum_p1 += this_update[len(this_update)//2]
    else:
        # Another observation for part 2: We don't have to actually order the list, we just need
        # to find the middle index. Since a correctly ordered update will have a "before count" that is
        # strictly decreasing by 1, the middle item will always be the item at len(before_list)//2.
        # So we just need to find the index of that number in before_list and then grab that item
        # from our update list.
        middle_index = before_list.index(len(before_list)//2)
        middle_sum_p2 += this_update[middle_index]

print(f"Part 1: {middle_sum_p1}")
print(f"Part 2: {middle_sum_p2}")
