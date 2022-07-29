from collections import Counter
import timeit
import datetime

start_time = datetime.datetime.now()
with open('puzzle_input.txt') as input_file:
    instruction_list = [str(input_line).strip() for input_line in input_file]
gamma = ''
epsilon = ''
for idx in range(len(instruction_list[0])):
    column_numbers = [number[idx] for number in instruction_list]
    bit_counts = Counter(column_numbers)
    gamma += '1' if bit_counts['1'] > bit_counts['0'] else '0'
    epsilon += '0' if bit_counts['1'] > bit_counts['0'] else '1'
print(int(gamma, 2) * int(epsilon,2))


end_time = datetime.datetime.now()
print(end_time - start_time)