with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip() for input_line in input_file]

increasing_counter = 0
for index in range(len(instruction_list)):
    if int(instruction_list[index]) > int(instruction_list[index-1]):
        increasing_counter += 1

print(increasing_counter)