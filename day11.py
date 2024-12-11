with open('input/11.txt') as f:
    stones = [int(x) for x in [line.rstrip() for line in f][0].split()]

iterations = 75
stone_states = dict()


def stone_transform(stone: int, i_count: int, st_states: dict) -> int:
    """
    A recursive function to transform stones. If the function reaches the ith transformation, it returns 1. If it
    detects a state we've already seen (stone, i_count) then it returns that count. Otherwise, it calls itself on
    the transformed stone or stones.
    :param stone: The number engraved on the current stone
    :param i_count: The count of times this stone has already transformed
    :param st_states: A dictionary of seen states. Key: (stone, i_count); value: count
    :return: stone_count: The total count of stones this stone gets transformed into
    """
    stone_count = 1
    # If we've reached the end, I am one stone. Return 1
    if i_count == iterations:
        st_states[stone, i_count] = stone_count
        return 1
    # If we've seen this state before, return that count instead
    if (stone, i_count) in st_states:
        return st_states[(stone, i_count)]

    # We still have transformations to do, so lets start transforming!
    # If stone == 0, update it to 1.
    if stone == 0:
        stone_count = stone_transform(1, i_count + 1, st_states)
    # If stone has even digits, split it
    elif len(str(stone)) % 2 == 0:
        first = int(str(stone)[0:len(str(stone))//2])
        second = int(str(stone)[len(str(stone))//2:])
        stone_count = (stone_transform(first, i_count + 1, st_states) +
                       stone_transform(second, i_count + 1, st_states))
    # Otherwise, multiply it by 2024
    else:
        stone_count = stone_transform(stone * 2024, i_count + 1, st_states)

    # Update our dictionary of states and return our total count
    st_states[stone, i_count] = stone_count
    return stone_count


total_count = 0
for this_stone in stones:
    total_count += stone_transform(this_stone, 0, stone_states)

print(f"After {iterations} transformations: {total_count}")
