import re

with open('puzzle_input.txt') as input_file:
    instructions = ''
    for line in input_file:
        line = line.strip()
        instructions += line

regex = r"mul\((\d+),(\d+)\)"
matched_mul = re.findall(regex, instructions)
total_sum = 0

for match in matched_mul:
    match = list(match)
    total_sum += int(match[0]) * int(match[1])

print(matched_mul)
print(total_sum)