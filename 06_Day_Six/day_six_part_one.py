import pprint

pp = pprint.PrettyPrinter(indent=4)
instruction_list = []
with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip() for input_line in input_file]

