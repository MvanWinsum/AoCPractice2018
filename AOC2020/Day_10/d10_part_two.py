with open('./puzzle_input.txt') as input_file:
    lines = [int(line.strip()) for line in input_file]
    lines.sort()
    lines.insert(0, 0)
    lines.append(max(lines) + 3)
    print(lines)

current_joltage = 0
change_distribution = [0, 0, 0]
paths = {}

def traverse_and_count(index):
    if index == len(lines) - 1:
        return 1
    if index in paths:
        return paths[index]
    num_paths = 0
    for step in range(index + 1, len(lines)):
        if lines[step] - lines[index] <= 3:
            num_paths += traverse_and_count(step)
    paths[index] = num_paths
    return num_paths


print(traverse_and_count(0))
