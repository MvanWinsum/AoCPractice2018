
with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip().split(',') for input_line in input_file][0]
    instruction_list = [int(timer) for timer in instruction_list]
    print(instruction_list)


def simulate_fish_day(fish):
    new_fish = False
    if fish == 0:
        fish = 6
        new_fish = True
    else:
        fish -= 1
    return fish, new_fish


def simulate_day(pool):
    for fish_idx in range(len(pool)):
        fish, new_fish = simulate_fish_day(pool[fish_idx])
        pool[fish_idx] = fish
        if new_fish:
            pool.append(8)
    return pool


for day in range(80):
    instruction_list = simulate_day(instruction_list)

print(len(instruction_list))