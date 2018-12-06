import pprint
pp = pprint.PrettyPrinter(indent=4)
with open('puzzle_input.txt') as input_file:
    input_letters = [input_line.strip() for input_line in input_file][0]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
pairs = [letter + letter.upper() for letter in alphabet]
pairs += [letter.upper() + letter for letter in alphabet]


while True:
    og_string_len = len(input_letters)
    for pair in pairs:
        input_letters = input_letters.replace(pair, '')
    if og_string_len == len(input_letters):
        break


pp.pprint(len(input_letters))
