import pprint
pp = pprint.PrettyPrinter(indent=4)
with open('puzzle_input.txt') as input_file:
    input_letters = [input_line.strip() for input_line in input_file][0]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
pairs = [letter + letter.upper() for letter in alphabet]
pairs += [letter.upper() + letter for letter in alphabet]
letter_lengths = {}


def collapse_polymer(collapse_input):
    while True:
        og_string_len = len(collapse_input)
        for pair in pairs:
            collapse_input = collapse_input.replace(pair, '')
        if og_string_len == len(collapse_input):
            return len(collapse_input)


for letter in alphabet:
    filtered_input = input_letters.replace(letter, '').replace(letter.upper(), '')
    letter_lengths[letter] = collapse_polymer(filtered_input)


pp.pprint(letter_lengths)
