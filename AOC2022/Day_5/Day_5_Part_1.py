from pprint import PrettyPrinter as ppr

# Parse the starting state of the stacks
stacks = [[], [], [], [], [], [], [], [], []]
stack_indices = [1, 5, 9, 13, 17, 21, 25, 29, 33]
with open('puzzle_input_stacks.txt') as input_file:
    lines = [line for line in input_file]
    for line in lines:
        for idx, stack_idx in enumerate(stack_indices):
            if len(line) >= stack_idx and line[stack_idx] != ' ':
                stacks[idx].append(line[stack_idx])

# Parse the moving instructions
# Instruction format: [amount of items] from [source_stack] to [destination_stack]
parsed_instructions = []
with open('puzzle_input_instructions.txt') as input_file:
    instruction_collection = [line.strip().split(' ') for line in input_file]
    for instruction in instruction_collection:
        parsed_instructions.append([int(instruction[1]), int(instruction[3]), int(instruction[5])])


# Start moving around the stacks
for instruction in parsed_instructions:
    for idx in range(instruction[0]):
        stacks[instruction[2]-1].insert(0, stacks[instruction[1]-1][0])
        del stacks[instruction[1]-1][0]

# Print Answer
answer = ''
for stack in stacks:
    answer += stack[0]
print(answer)
