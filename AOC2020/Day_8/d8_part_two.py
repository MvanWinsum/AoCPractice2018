
with open('./puzzle_input.txt') as input_file:
    instructions = [instruction.strip().split(' ') for instruction in input_file.readlines()]


def run_instructions(instructions):
    instruction_index = 0
    accumulator = 0
    completed_instructions = []
    while instruction_index not in completed_instructions:
        completed_instructions.append(instruction_index)
        if instructions[instruction_index][0] == 'nop':
            instruction_index += 1
        elif instructions[instruction_index][0] == 'acc':
            accumulator += int(instructions[instruction_index][1])
            instruction_index += 1
        elif instructions[instruction_index][0] == 'jmp':
            instruction_index += int(instructions[instruction_index][1])
        if instruction_index >= len(instructions):
            return accumulator, True
    return accumulator, False
print(run_instructions(instructions))


for jump_index in range(len(instructions)):
    if 'jmp' in instructions[jump_index]:
        instructions[jump_index][0] = 'nop'
    acc, found = run_instructions(instructions)
    if found:
        print(acc)
        break
    else:
        instructions[jump_index][0] = 'jmp'

