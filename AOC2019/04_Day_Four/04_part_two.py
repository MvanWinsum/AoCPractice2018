from collections import Counter
numbers_to_check = range(206938, 679128)
valid_numbers_part_one = []
valid_numbers_part_two = []


def check_number(number):
    adjacent = False
    increase = True
    for idx, digit in enumerate(str(number)):
        if idx != len(str(number)) - 1:
            adjacent = True if str(number)[idx + 1] == digit else adjacent
            if int(str(number)[idx + 1]) < int(digit):
                increase = False
                break
    return adjacent, increase


for number in numbers_to_check:
    adjacent, increase = check_number(number)
    if increase is True and adjacent is True:
        valid_numbers_part_one.append(number)
for potential_number in valid_numbers_part_one:
    characters = Counter(str(potential_number)).values()
    if 2 in characters:
        valid_numbers_part_two.append(potential_number)


# Part 1
print('Part One: {}'.format(len(valid_numbers_part_one)))

# Part 2
print('Part Two: {}'.format(len(valid_numbers_part_two)))