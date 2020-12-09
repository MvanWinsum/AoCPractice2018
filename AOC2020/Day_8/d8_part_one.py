
with open('./puzzle_input.txt') as input_file:
    instructions = [instruction.strip().split(' ') for instruction in input_file.readlines()]
    print(len(instructions))

instruction_index = 0
accumulator = 0
completed_instructions = []

while instruction_index not in completed_instructions:
    print("Instruction: %s | Accumulator: %s | Index: %d" % (instructions[instruction_index], accumulator, instruction_index))
    completed_instructions.append(instruction_index)
    if instructions[instruction_index][0] == 'nop':
        instruction_index += 1
    elif instructions[instruction_index][0] == 'acc':
        accumulator += int(instructions[instruction_index][1])
        instruction_index += 1
    elif instructions[instruction_index][0] == 'jmp':
        instruction_index += int(instructions[instruction_index][1])
    print(completed_instructions)

print(
    "Instruction: %s | Accumulator: %s | Index: %d" % (instructions[instruction_index], accumulator, instruction_index))