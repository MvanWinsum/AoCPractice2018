with open('puzzle_input.txt') as input_file:
    calibrations = [line.strip() for line in input_file]


fixed_calibrations = []

for calibration in calibrations:
	current_digits = []
	for symbol in calibration:
		if symbol.isnumeric():
			current_digits.append(symbol)
	fixed_line = int(current_digits[0] + current_digits[len(current_digits) - 1])
	fixed_calibrations.append(fixed_line)

print(sum(fixed_calibrations))