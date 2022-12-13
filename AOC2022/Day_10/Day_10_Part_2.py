with open('puzzle_input.txt') as input_file:
    operations = [line.strip().split(' ') for line in input_file]
    print(operations)

cycle_counter = 0
program_value = 1

cycle_values = []

for operation in operations:
    for operation_part in operation:
        if program_value in range(cycle_counter-1, cycle_counter+2):
            cycle_values.append("#")
        else:
            cycle_values.append('.')
        try:
            update_value_amount = int(operation_part)
            program_value += update_value_amount
        except ValueError:
            pass
        cycle_counter += 1
        cycle_counter = cycle_counter % 40


answer_indices = [0, 40, 80, 120, 160, 200]
answer = 0
for idx in answer_indices:
    print(' '.join(cycle_values[idx:idx+39]))