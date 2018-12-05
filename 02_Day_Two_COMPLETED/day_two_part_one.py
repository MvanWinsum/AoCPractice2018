import pprint, collections
pp = pprint.PrettyPrinter(indent=4)

two_appearances = 0
three_appearances = 0

with open('puzzle_input.txt') as input_file:
    box_list = [input_line.strip() for input_line in input_file]

for box in box_list:
    d = collections.Counter(box)
    if 2 in d.values():
        two_appearances += 1
    if 3 in d.values():
        three_appearances += 1

pp.pprint(two_appearances)
pp.pprint(three_appearances)