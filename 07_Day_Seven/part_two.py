import pprint
pp = pprint.PrettyPrinter(indent=4)
with open('puzzle_input.txt') as input_file:
    input_letters = [input_line.strip() for input_line in input_file][0]
