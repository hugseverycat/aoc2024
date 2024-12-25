with open('input/25.txt') as f:
    lines = [line.rstrip() for line in f]

keys = []
locks = []
new_schematic = True
schematic_type = None

for this_line in lines:
    if new_schematic:
        new_schematic = False
        this_schematic = [0, 0, 0, 0, 0]
        if this_line == '#####':
            schematic_type = 'lock'
        else:
            schematic_type = 'key'
    elif this_line == '':
        new_schematic = True
        if schematic_type == 'lock':
            locks.append(this_schematic)
        else:
            this_schematic = [x - 1 for x in this_schematic]
            keys.append(this_schematic)
    else:
        for i, this_char in enumerate(this_line):
            if this_char == '#':
                this_schematic[i] += 1

if schematic_type == 'lock':
    locks.append(this_schematic)
else:
    this_schematic = [x - 1 for x in this_schematic]  # Removing the row with all #s
    keys.append(this_schematic)

valid_combinations = 0
for this_key in keys:
    for this_lock in locks:
        if [(sum(x) <= 5) for x in zip(this_key, this_lock)] == [True, True, True, True, True]:
            valid_combinations += 1
print(f"Part 1: {valid_combinations}")
