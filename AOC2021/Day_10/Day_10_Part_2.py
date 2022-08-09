with open('puzzle_input.txt') as input_file:
    instruction_list = [list(input_line.strip()) for input_line in input_file]

incomplete_line_scores = []

symbol_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

closing_symbols = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def calculate_closer_score(closer_string):
    score = 0
    for symbol in closer_string:
        score = score * 5
        score += symbol_scores[symbol]
    return score


for symbol_line in instruction_list:
    opening_symbols = ''
    valid_line = True
    for symbol in symbol_line:
        if symbol not in closing_symbols:
            opening_symbols += symbol
        else:
            if opening_symbols[-1] is not closing_symbols[symbol]:
                valid_line = False
                break
            else:
                opening_symbols = opening_symbols[:-1]
    if valid_line:
        required_closers = opening_symbols[::-1].replace('(', ')').replace('{', '}').replace('[', ']').replace('<', '>')
        incomplete_line_scores.append(calculate_closer_score(required_closers))

incomplete_line_scores.sort()
print(incomplete_line_scores[int(len(incomplete_line_scores)/2)])
