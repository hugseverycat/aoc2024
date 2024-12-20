with open('input/19.txt') as f:
    lines = [line.rstrip() for line in f]

towels = []
patterns = []
pattern_cache = dict()
switch = False
for this_line in lines:
    if switch:
        patterns.append(this_line)
    elif this_line == '':
        switch = True
    else:
        towels = this_line.split(', ')


def find_pattern(pattern_to_find: str) -> int:
    """
    A recursive function that finds how many ways there are to create the pattern provided. If the towel's pattern
    matches the start of the pattern we're analyzing, those characters are removed and the remaining pattern is passed
    back into the function.
    :param pattern_to_find: The pattern we are analyzing
    :return: An integer count of the number of ways that pattern can be created with the available towels.
    """
    if pattern_to_find == '':
        # If the pattern is empty, then we have successfully created this pattern. Return 1.
        return 1
    if pattern_to_find in pattern_cache:
        # Check the cache to see if we've already analyzed this pattern.
        return pattern_cache[pattern_to_find]
    # This is a new pattern, so we'll start counting matches
    matches = 0
    for towel in towels:
        # Check each towel to see if it is at the beginning of the pattern we're looking for
        if pattern_to_find.startswith(towel):
            # If so, we will send the rest of the pattern back into the recursive function
            new_pattern = pattern_to_find[len(towel):]
            matches += find_pattern(new_pattern)
    # Save the result in the cache and then return the result.
    pattern_cache[pattern_to_find] = matches
    return matches


counter_p1 = 0
counter_p2 = 0
for this_pattern in patterns:
    temp_counter = find_pattern(this_pattern)
    if temp_counter:
        # If no matches were found, don't count it for part 1
        counter_p1 += 1
        counter_p2 += temp_counter

print(f"Part 1: {counter_p1}")
print(f"Part 2: {counter_p2}")
