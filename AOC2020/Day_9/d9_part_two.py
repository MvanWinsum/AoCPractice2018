import numpy as np

with open('./puzzle_input.txt') as input_file:
    lines = [int(line.strip()) for line in input_file]


def find_contiguous_set(number):
    for index_lower in range(0, len(lines)):
        for index_upper in range(1, len(lines)):
            set = np.array(lines[index_lower:index_upper])
            if set.sum() > number:
                break
            if set.sum() == number and len(set) > 1:
                return set


for index in range(26,len(lines)):
    candidates = lines[index - 25:index]
    valid_number = False
    for candidate in candidates:
        if lines[index] - candidate in candidates:
            valid_number = True
    if not valid_number:
        part_two_answer = find_contiguous_set(lines[index])
        print("Number to combine: %d" % lines[index])
        print("Answer: %d %d \n Sum: %d" %
              (part_two_answer.min(),
               part_two_answer.max(),
              (part_two_answer.min() + part_two_answer.max())))
        break
