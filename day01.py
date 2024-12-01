with open('input/01.txt') as f:
    lines = [line.rstrip() for line in f]

left_list = []
right_list = []
for this_line in lines:
    l, r = [int(x) for x in this_line.split()]
    left_list.append(l)
    right_list.append(r)

left_list.sort()
right_list.sort()

difference = 0
sim_score = 0
for i, loc_ID in enumerate(left_list):
    difference += abs(left_list[i] - right_list[i])
    sim_score += left_list[i] * right_list.count(left_list[i])

print(f"Part 1: {difference}")
print(f"Part 2: {sim_score}")
