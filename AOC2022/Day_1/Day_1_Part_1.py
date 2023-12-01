with open('puzzle_input.txt') as input_file:
    carry_collection = [line.strip() for line in input_file]
print(carry_collection)
current_highest = 0
current_carrying = 0

for element in carry_collection:
    if element == '':
        if current_carrying > current_highest:
            current_highest = current_carrying
        current_carrying = 0
        continue
    else:
        current_carrying += int(element)

print(current_highest)
