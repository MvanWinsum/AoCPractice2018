with open('puzzle_input.txt') as input_file:
    calibrations = [line.strip() for line in input_file]

fixed_calibrations = []
number_transliterations = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

for calibration in calibrations:
    current_digits = []
    potential_transliterations = []
    print(f'Original: {calibration}')
    for key in number_transliterations:
        number_index = calibration.find(key)
        if number_index > -1:
            potential_transliterations.append((key, number_index))
    potential_transliterations.sort(key=lambda x: x[1])
    for number, index in potential_transliterations:
        calibration = calibration.replace(number, number_transliterations[number])
    print(f'Changed: {calibration}')
    for symbol in calibration:
        if symbol.isnumeric():
            current_digits.append(symbol)
    print(current_digits)
    fixed_line = int(current_digits[0] + current_digits[len(current_digits) - 1])
    fixed_calibrations.append(fixed_line)

print(sum(fixed_calibrations))
