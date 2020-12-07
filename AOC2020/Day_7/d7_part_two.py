with open('puzzle_input.txt') as input_file:
    instructions = [line.strip() for line in input_file.readlines()]


def get_num_containing_bags(colour):
    relevant_lines = [line for line in instructions if colour in line and line.index(colour) == 0]
    total_bags_inside = 0
    for line in relevant_lines:
        contains = line.split(' contain ')[1].split(', ')
        for bag in contains:
            bag = bag.split(' ')
            if bag[0] != 'no':
                num_bags_inside = int(bag[0])
                bag_colour = ' '.join(bag[1:3])
                total_bags_inside += num_bags_inside
                total_bags_inside += num_bags_inside * get_num_containing_bags(bag_colour)
    return total_bags_inside


print(get_num_containing_bags('shiny gold'))
