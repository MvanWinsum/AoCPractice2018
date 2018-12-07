import pprint

pp = pprint.PrettyPrinter(indent=4)
frequency = 0
frequency_list = {}
instruction_list = []
continue_loop = True
with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip() for input_line in input_file]