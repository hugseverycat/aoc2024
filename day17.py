import re

with open('input/sample.txt') as f:
    lines = [line.rstrip() for line in f]

def to_base8(convert: int):
    n = oct(convert)[2:]
    return int(n)

def to_base10(convert: int):
    convert = str(convert)
    return int(convert, 8)



program = [int(x) for x in lines[4][9:].split(',')]
register_a = int(re.findall('\d+', lines[0])[0])
register_b = 0
register_c = 0
inst_pointer = 0
output = ''
"""
    Combo operands 0 through 3 represent literal values 0 through 3.
    Combo operand 4 represents the value of register A.
    Combo operand 5 represents the value of register B.
    Combo operand 6 represents the value of register C.
    Combo operand 7 is reserved and will not appear in valid programs.
"""
def combo_op(operand):
    assert operand != 7
    if operand <= 3:
        return operand
    if operand == 4:
        return register_a
    if operand == 5:
        return register_b
    if operand == 6:
        return register_c
"""
The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found
by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand 
of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A 
register."""
def adv(operand):  # opcode 0
    global register_a, inst_pointer
    print(f"  opcode 0; operand {operand}: reg_a {register_a} -> {register_a} // (2 ** {combo_op(operand)}) = "
          f"{register_a // (2 ** combo_op(operand))}")
    register_a = register_a // (2 ** combo_op(operand))
    inst_pointer += 2
"""
The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then 
stores the result in register B.
"""
def bxl(operand):  # opcode 1
    global register_b, inst_pointer
    print(f"  opcode 1: operand {operand}: reg_b {register_b} -> {operand} ^ {register_b} = {operand ^ register_b}")
    register_b = operand ^ register_b
    inst_pointer += 2
"""
The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 
bits), then writes that value to the B register."""
def bst(operand):  # opcode 2
    global register_b, inst_pointer
    print(f"  opcode 2: operand {operand}: reg_b {register_b} -> {combo_op(operand)} % 8 = {combo_op(operand) % 8}")
    register_b = combo_op(operand) % 8
    inst_pointer += 2
"""
The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by 
setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer 
is not increased by 2 after this instruction."""
def jnz(operand):  # opcode 3
    global register_a, inst_pointer

    if register_a == 0:
        print(f"  opcode 3: operand {operand}: since reg_a == 0, doing nothing")
        inst_pointer += 2
    else:
        print(f"  opcode 3: operand {operand}: jump to pointer {operand}")
        inst_pointer = operand
"""
The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in 
register B. (For legacy reasons, this instruction reads an operand but ignores it.)"""
def bxc(operand: None):  # opcode 4
    global register_b, register_c, inst_pointer
    print(f"  opcode 4: operand {operand}: reg_b {register_b} -> reg_b {register_b} ^ reg_c {register_c} = {register_b ^ register_c}")
    register_b = register_b ^ register_c
    inst_pointer += 2
"""
The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a 
program outputs multiple values, they are separated by commas.)"""
def out(operand):  # opcode 5
    global inst_pointer, output
    inst_pointer += 2
    print(f"  opcode 5: outputting combo_op({operand}) % 8 = {combo_op(operand) % 8}")
    if output == '':
        output += str(combo_op(operand) % 8)
    else:
        output += ',' + str(combo_op(operand) % 8)
"""
The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B 
register. (The numerator is still read from the A register.)"""
def bdv(operand):  # opcode 6
    global register_a, register_b, inst_pointer
    print(f"  opcode 0; operand {operand}: reg_b {register_b} -> {register_a} // (2 ** {combo_op(operand)}) = "
          f"{register_a // (2 ** combo_op(operand))}")
    register_b = register_a // (2 ** combo_op(operand))
    inst_pointer += 2
"""
The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C 
register. (The numerator is still read from the A register.)
"""
def cdv(operand):  # opcode 7
    global register_a, register_c, inst_pointer
    print(f"  opcode 7; operand {operand}: reg_c {register_c} -> {register_a} // (2 ** {combo_op(operand)}) = "
          f"{register_a // (2 ** combo_op(operand))}")
    register_c = register_a // (2 ** combo_op(operand))
    inst_pointer += 2

registers = []
counter = 0
for a in [register_a]:
    print(f"Running program {program} with register_a set to {a} ({to_base8(a)}): ")
    register_a = a
    register_b = 0
    register_c = 0
    inst_pointer = 0
    output = ''
    while inst_pointer < len(program):
        opcode = program[inst_pointer]
        op = program[inst_pointer + 1]
        if opcode == 0:
            adv(op)
        elif opcode == 1:
            bxl(op)
        elif opcode == 2:
            bst(op)
        elif opcode == 3:
            jnz(op)
        elif opcode == 4:
            bxc(op)
        elif opcode == 5:
            out(op)
            print(f"Writing output at step {counter}")
            ab8 = to_base8(register_a)
            bb8 = to_base8(register_b)
            cb8 = to_base8(register_c)
            print(f"Register A is now {register_a} ({ab8}). B = {register_b}"
                  f" ({bb8}). C = {register_c} ({cb8})")

        elif opcode == 6:
            bdv(op)
        elif opcode == 7:
            cdv(op)
        counter += 1

    registers.append(f"Register A: {a}; Output: {output}")

for r in registers:
    print(r)

