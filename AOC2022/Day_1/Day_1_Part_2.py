import numpy as np

with open('puzzle_input.txt') as input_file:
    carry_collection = [line.strip() for line in input_file]

current_highest = []
current_carrying = 0

for element in carry_collection:
    if element == '':
        current_highest.append(current_carrying)
        current_carrying = 0
        continue
    else:
        current_carrying += int(element)

current_highest.sort(reverse=True)
print(np.array(current_highest[0:3]).sum())
