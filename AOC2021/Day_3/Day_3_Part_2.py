from collections import Counter

with open('puzzle_input.txt') as input_file:
    instruction_list = [str(input_line).strip() for input_line in input_file]

oxygen_numbers = instruction_list.copy()
co2_numbers = instruction_list.copy()

for idx in range(len(instruction_list[0])):
    column_numbers = [number[idx] for number in instruction_list]
    bit_counts = Counter(column_numbers)
    most_common = 1 if bit_counts['1'] >= bit_counts['0'] else 0
    least_common = 1 - most_common
    if len(oxygen_numbers) > 1:
        column_numbers = [number[idx] for number in oxygen_numbers]
        bit_counts = Counter(column_numbers)
        most_common = '1' if bit_counts['1'] >= bit_counts['0'] else '0'
        oxygen_numbers = [number for number in oxygen_numbers if list(number)[idx] == most_common]
    if len(co2_numbers) > 1:
        column_numbers = [number[idx] for number in co2_numbers]
        bit_counts = Counter(column_numbers)
        least_common = '0' if bit_counts['1'] >= bit_counts['0'] else '1'
        co2_numbers = [number for number in co2_numbers if list(number)[idx] == least_common]
    if len(oxygen_numbers) == 1 and len(co2_numbers) == 1:
        break

print(int(oxygen_numbers[0], 2) * int(co2_numbers[0],2))
