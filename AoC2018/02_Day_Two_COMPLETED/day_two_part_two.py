import pprint
pp = pprint.PrettyPrinter(indent=4)

two_appearances = 0
three_appearances = 0

with open('puzzle_input.txt') as input_file:
    box_list = [input_line.strip() for input_line in input_file]
iterations = 0
for box in box_list:
    for other_box in box_list:
        differences = 0
        for index in range(len(box.strip())):
            box_letter = box[index]
            if box_letter != other_box.strip()[index]:
                differences += 1
        if differences == 1:
            pp.pprint('THESE ARE THE BOXES --> BOX 1: ' + box + '  | BOX 2: ' + other_box)
            break
        iterations += 1
    iterations += 1

pp.pprint(iterations)
