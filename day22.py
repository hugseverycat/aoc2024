with open('input/22.txt') as f:
    lines = [line.rstrip() for line in f]

secret_numbers = [int(x) for x in lines]
evolved_numbers = []
evolutions = 2000


def mix_numbers(secret_num: int, mix_num: int) -> int:
    return secret_num ^ mix_num


def prune(secret_num: int) -> int:
    return secret_num % 16777216


def evolve_number(int_to_evolve: int) -> int:
    # Step 1: Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret
    # number. Finally, prune the secret number.
    mult_64 = int_to_evolve * 64
    int_to_evolve = mix_numbers(int_to_evolve, mult_64)
    int_to_evolve = prune(int_to_evolve)

    # Step 2: Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
    # Then, mix this result into the secret number. Finally, prune the secret number.
    div_32 = int_to_evolve // 32
    int_to_evolve = mix_numbers(int_to_evolve, div_32)
    int_to_evolve = prune(int_to_evolve)

    # Step 3: Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret
    # number. Finally, prune the secret number.
    mult_2048 = int_to_evolve * 2048
    int_to_evolve = mix_numbers(int_to_evolve, mult_2048)
    return prune(int_to_evolve)


evolution_sum = 0
sequences = []
for this_number in secret_numbers:
    evolved = this_number
    for i in range(evolutions):
        evolved = evolve_number(evolved)
    evolution_sum += evolved
print(f"Part 1: {evolution_sum}")
