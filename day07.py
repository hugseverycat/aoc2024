with open('input/07.txt') as f:
    lines = [line.rstrip() for line in f]

equations = []
for line in lines:
    temp_line = line.split()
    equations.append([int(temp_line[0][:-1])] + [int(x) for x in temp_line[1:]])


def do_math(current_value: int, value_list: list, operation: str, goal: int) -> bool:
    """
    :param current_value: The result of any operations we've already done
    :param value_list: The remaining numbers to add, multiply, or concatenate
    :param operation: '+', '*', or '|'
    :param goal: The number we are trying to reach
    :return: bool

    This recursive function returns True if current_value == goal and value_list is empty.
    It returns False if we've exceeded the goal at any time, or if value_list is empty and current_value != goal.
    If none of these happen, it will update current_value using the current operation then call itself.
    """
    if current_value > goal:
        # If we're already too high, stop trying, return False
        return False
    if not value_list and current_value == goal:
        # If we've reached the end of the list and we've hit our goal, return True
        return True
    elif not value_list:
        # If we've reached the end of the list and we haven't hit our goal, return False
        return False
    else:
        # If we still have farther to go, perform the operation against the first value in the list
        if operation == '*':
            current_value = current_value * value_list[0]
        elif operation == '+':
            current_value = current_value + value_list[0]
        elif operation == '|':
            current_value = int(str(current_value) + str(value_list[0]))
        else:
            print(f"Unknown operation: {operation}")
        # Recursively send the new current value for multiplication and addition and concatenation
        return ((do_math(current_value, value_list[1:], '*', goal) or
                do_math(current_value, value_list[1:], '+', goal)) or
                do_math(current_value, value_list[1:], '|', goal))


counter = 0
for number_set in equations:
    goal_num = number_set[0]
    first = number_set[1]
    next_values = number_set[2:]
    if ((do_math(first, next_values, '*', goal_num) or
            do_math(first, next_values, '+', goal_num)) or
            do_math(first, next_values, '|', goal_num)):
        counter += goal_num
print(f"Part 2: {counter}")
