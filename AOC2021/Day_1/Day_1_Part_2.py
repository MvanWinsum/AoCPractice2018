with open('puzzle_input.txt') as input_file:
    instruction_list = [int(input_line.strip()) for input_line in input_file]

previous_three = instruction_list[0] + instruction_list[1] + instruction_list[2]
increasing_counter = 0
for index in range(3, len(instruction_list)):
    current_three = instruction_list[index-2] + instruction_list[index-1] + instruction_list[index]
    if current_three > previous_three:
        increasing_counter += 1
    previous_three = current_three

print(increasing_counter)
