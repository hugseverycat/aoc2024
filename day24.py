from collections import deque

with open('input/24.txt') as f:
    lines = [line.rstrip() for line in f]

bits = dict()
operations = deque()
switch = False


for this_line in lines:
    if this_line == '':
        switch = True
    elif not switch:
        this_bit, this_value = this_line.split(': ')
        this_value = int(this_value)
        bits[this_bit] = this_value
    else:
        # ktr AND qkd -> cgm
        first_operand, operation, second_operand, _, result = this_line.split()
        if first_operand and second_operand in bits:
            operations.append([first_operand, second_operand, operation, result])
        else:
            operations.append([first_operand, second_operand, operation, result])

while operations:
    first_operand, second_operand, operation, result = operations.popleft()
    if first_operand in bits and second_operand in bits:
        if operation == 'AND':
            bits[result] = bits[first_operand] and bits[second_operand]
        elif operation == 'OR':
            bits[result] = bits[first_operand] or bits[second_operand]
        elif operation == 'XOR':
            bits[result] = bits[first_operand] != bits[second_operand]
    else:
        operations.append([first_operand, second_operand, operation, result])

z_bits = []
x_bits = []
y_bits = []
for this_bit in bits:
    if this_bit.startswith('z'):
        z_bits.append(this_bit)
    elif this_bit.startswith('x'):
        x_bits.append(this_bit)
    elif this_bit.startswith('y'):
        y_bits.append(this_bit)
z_output = ''
x_value = ''
y_value = ''
x_bits.sort(reverse=True)
y_bits.sort(reverse=True)
z_bits.sort(reverse=True)
for z_bit in z_bits:
    z_output += str(int(bits[z_bit]))
for x_bit in x_bits:
    x_value += str(int(bits[x_bit]))
for y_bit in y_bits:
    y_value += str(int(bits[y_bit]))

print(f"Part 1: {int(z_output, 2)}")
