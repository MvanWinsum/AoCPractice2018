fuel_needed = 0


def fuel_for_module(mass):
    return int(mass / 3) - 2


with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip() for input_line in input_file]
    for module in instruction_list:
        fuel_needed += fuel_for_module(int(module))
print(fuel_needed)