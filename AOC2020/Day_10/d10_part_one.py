with open('./puzzle_input.txt') as input_file:
    lines = [int(line.strip()) for line in input_file]
    lines.sort()
    lines.append(max(lines) + 3)
    print(lines)

current_joltage = 0
change_distribution = [0, 0, 0]

while len(lines) > 0:
    next_adapter = lines.pop(0)
    change_distribution[(next_adapter - current_joltage) - 1] += 1
    current_joltage = next_adapter

print(change_distribution)
