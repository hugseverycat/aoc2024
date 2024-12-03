import re

with open('input/03.txt') as f:
    lines = [line.rstrip() for line in f]


def find_multiply_pairs(find_line):
    # Takes a line of instructions, locates all mul(x,y), multiplies each x and y
    # then returns the sum
    p_sum = 0
    p_list = re.findall("mul\((\d+,\d+)\)", find_line)
    for pair in p_list:
        int_pair = [int(a) for a in pair.split(",")]
        p_sum += int_pair[0] * int_pair[1]
    return p_sum

# Part 1
mul_result = 0
mega_line = ""
for line in lines:
    mega_line += line  # Part 2 is a lot easier if the input is all on one line
mul_result = find_multiply_pairs(mega_line)
print(f"Part 1: {mul_result}")

# Part 2
mul_result = 0
# Split the line by "don't()". Then the beginning of each group (after the first group)
# will not be doing multiplications
inst_blocks = mega_line.split("don't()")

# Start by finding all the multiplications at the beginning, when do() is on
mul_result += find_multiply_pairs(inst_blocks[0])

for n in range(1, len(inst_blocks)):
    # Each of these inst_blocks starts with don't()
    # Find where do() gets turned back on
    i = inst_blocks[n].find('do()')

    # Create a substring where do() is on
    do_string = inst_blocks[n][i:]

    # Find all the multiplications
    mul_result += find_multiply_pairs(do_string)

print(f"Part 2: {mul_result}")
