
for noun in range(1, 100):
    for verb in range(1, 100):
        current_index = 0
        with open('puzzle_input.txt') as input_file:
            instruction_list = [int(x) for x in input_file.readline().split(",")]
            instruction_list[1] = noun
            instruction_list[2] = verb
            while current_index < len(instruction_list):
                n1, n2, n3 = instruction_list[current_index + 1], instruction_list[current_index + 2], instruction_list[current_index + 3]
                if instruction_list[current_index] == 1:
                    instruction_list[n3] = instruction_list[n1] + instruction_list[n2]
                elif instruction_list[current_index] == 2:
                    instruction_list[n3] = instruction_list[n1] * instruction_list[n2]
                elif instruction_list[current_index] == 99:
                    if instruction_list[0] == 19690720:
                        print('--------------> TARGET NOUN: {}, TARGET VERB: {}, Answer: {}'.format(noun, verb, str(100 * noun + verb)))
                    print('Noun: {}, Verb: {}, Value at zero: {} '.format(noun, verb, str(instruction_list[0])))
                    break
                current_index += 4

print(instruction_list)
