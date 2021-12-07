import numpy as np

with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip().split(',') for input_line in input_file][0]
    instruction_list = [int(position) for position in instruction_list]


def get_needed_fuel(positions, target):
    fuel_needed = 0
    for position in positions:
        fuel_needed += abs(position - target)
    return fuel_needed


current_index = int(np.average(instruction_list))
up = True
down = True

while up or down:
    current_score = get_needed_fuel(instruction_list, current_index)
    if up:
        up_score = get_needed_fuel(instruction_list, current_index+1)
        up = up_score < current_score
        if up:
            current_index += 1
            continue
    if down:
        down_score = get_needed_fuel(instruction_list, current_index-1)
        down = down_score < current_score
        if down:
            current_index -= 1
            continue
print(f'current_index: {current_index} Score: {get_needed_fuel(instruction_list, current_index)} '
      f'Up: {get_needed_fuel(instruction_list, current_index+1)} '
      f'Down: {get_needed_fuel(instruction_list, current_index-1)}')