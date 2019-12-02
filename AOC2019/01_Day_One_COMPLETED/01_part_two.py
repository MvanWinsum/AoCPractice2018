fuel_needed = 0


def fuel_for_module(mass):
    fuel_for_mass = mass // 3 - 2
    if fuel_for_mass > 0:
        fuel_for_mass += fuel_for_module(fuel_for_mass)
        return fuel_for_mass
    else:
        return 0


with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip() for input_line in input_file]
    for module_mass in instruction_list:
        fuel_needed += fuel_for_module(int(module_mass))
print(fuel_needed)