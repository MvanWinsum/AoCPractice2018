with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip().split(' ') for input_line in input_file]

horizontal = 0
depth = 0
aim = 0

for instruction in instruction_list:
    if instruction[0] == 'forward':
        horizontal += int(instruction[1])
        depth += int(instruction[1]) * aim
    elif instruction[0] == 'up':
        aim -= int(instruction[1])
    elif instruction[0] == 'down':
        aim += int(instruction[1])

print(f'horizontal: {horizontal} depth: {depth} answer: {(horizontal * depth)}')