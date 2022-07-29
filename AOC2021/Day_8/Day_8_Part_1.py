
# Sections needed -> One: 2 segments    Four: 4 segments    Seven: 3 segments   Eight: 7 segments

with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip().split(' | ')[1].split(' ') for input_line in input_file]
    instruction_list = [[len(segment) for segment in line] for line in instruction_list]
    part_1_answer = 0
    for output in instruction_list:
        for number_length in output:
            if number_length in [2,4,3,7]:
                part_1_answer += 1
    print(part_1_answer)