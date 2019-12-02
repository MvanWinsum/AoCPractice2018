current_index = 0
with open('puzzle_input.txt') as input_file:
    instruction_list = [int(x) for x in input_file.readline().split(",")]
    instruction_list[1] = 12
    instruction_list[2] = 2
    while current_index < len(instruction_list):
        n1, n2, n3 = instruction_list[current_index + 1], instruction_list[current_index + 2], instruction_list[current_index + 3]
        if instruction_list[current_index] == 1:
            instruction_list[n3] = instruction_list[n1] + instruction_list[n2]
        elif instruction_list[current_index] == 2:
            instruction_list[n3] = instruction_list[n1] * instruction_list[n2]
        elif instruction_list[current_index] == 99:
            print('Value at the start of the intcode: ' + str(instruction_list[0]))
            break
        current_index += 4

print(instruction_list)
