numbers_to_check = range(206938, 679128)
valid_numbers = 0


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
        print(number)
        valid_numbers += 1

print(valid_numbers)