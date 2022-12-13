with open('puzzle_input.txt') as input_file:
    operations = [line.strip().split(' ') for line in input_file]
    print(operations)

cycle_counter = 0
program_value = 1

cycle_values = []

for operation in operations:
    for operation_part in operation:
        cycle_values.append(program_value)
        try:
            update_value_amount = int(operation_part)
            program_value += update_value_amount
        except ValueError:
            pass

answer_indices = [19, 59, 99, 139, 179, 219]
answer = 0
for idx in answer_indices:
    answer += (idx+1) * cycle_values[idx]
print(answer)