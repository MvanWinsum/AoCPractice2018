with open('puzzle_input.txt') as input_file:
    instruction_list = [list(input_line.strip()) for input_line in input_file]

first_invalid_symbols = []

symbol_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

closing_symbols = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

for symbol_line in instruction_list:
    opening_symbols = ''
    for symbol in symbol_line:
        if symbol not in closing_symbols:
            opening_symbols += symbol
        else:
            if opening_symbols[-1] is not closing_symbols[symbol]:
                first_invalid_symbols.append(symbol)
                break
            else:
                opening_symbols = opening_symbols[:-1]

invalid_score = 0
for invalid_symbol in first_invalid_symbols:
    invalid_score += symbol_scores[invalid_symbol]

print(invalid_score)