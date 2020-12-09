with open('./puzzle_input.txt') as input_file:
    lines = [int(line.strip()) for line in input_file]

for index in range(26,len(lines)):
    candidates = lines[index - 25:index]
    valid_number = False
    for candidate in candidates:
        if lines[index] - candidate in candidates:
            print("Next number: %d | Composites: %d <-> %d" % (lines[index], candidate, lines[index] - candidate))
            valid_number = True
    if not valid_number:
        print("Answer: %d" % lines[index])
        break