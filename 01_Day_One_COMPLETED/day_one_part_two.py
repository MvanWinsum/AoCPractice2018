import pprint

pp = pprint.PrettyPrinter(indent=4)
frequency = 0
frequency_list = {}
instruction_list = []
continue_loop = True
with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip() for input_line in input_file]

while continue_loop is True:
    for input_line in instruction_list:
        frequency = frequency + int(input_line)
        if frequency_list.get(frequency) is not None:
            pp.pprint("----------------------> THIS IS THE FREQUENCY: " + str(frequency))
            continue_loop = False
            break
        frequency_list[frequency] = 1
        pp.pprint(frequency)


