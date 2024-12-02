with open('input/02.txt') as f:
    lines = [line.rstrip() for line in f]


def check_safety(check_report: list, remove_index=None):
    # This function is recursive. If the function compares two numbers and the safety rules
    # are broken, it will call itself twice more, to see if the report is safe if n or n+1 is
    # removed.
    if remove_index is not None:
        if remove_index < 0:
            # Make sure we're checking a valid index
            return False
        # If remove_index is not None, then we are doing a safety check with a number removed
        # So remove that number from the list
        temp_list = [x for x in check_report]
        del temp_list[remove_index]
        check_report = [x for x in temp_list]
        # The above lines copy the list with the item removed, without altering the original list
    safe = True

    # First establish whether the list is increasing
    if check_report[1] > check_report[0]:
        increasing = True
    else:
        increasing = False

    # We will now compare each item to its neighbor
    for n in range(0, len(check_report) - 1):
        difference = abs(check_report[n+1] - check_report[n])
        if not 1 <= difference <= 3:
            safe = False
        elif increasing and check_report[n+1] < check_report[n]:
            safe = False
        elif not increasing and check_report[n+1] > check_report[n]:
            safe = False
        if not safe:
            if remove_index is None:
                # Since we haven't removed anything yet, check the safety of the report
                # with n, n+1, and n-1 removed. If one of them is safe, then the report is safe
                return (check_safety(check_report, n) or check_safety(check_report, n+1)
                        or check_safety(check_report, n-1))
            else:
                # remove_index is not None, so we've failed safety checks AND this is already
                # checking a list with a removed index. so it is definitely not safe and we can
                # break out of the for loop.
                break
    return safe


safe_counter = 0
for this_line in lines:
    report = [int(x) for x in this_line.split()]
    if check_safety(report):
        safe_counter += 1

print(f"Part 2: {safe_counter}")
