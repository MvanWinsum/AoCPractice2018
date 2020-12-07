with open('puzzle_input.txt') as input_file:
    instructions = [line.strip() for line in input_file.readlines()]


def get_num_bags(color):
    relevant_lines = [line for line in instructions if color in line and line.index(color) != 0]
    colours_found = []
    if len(relevant_lines) == 0:
        return []
    else:
        new_colours = list(set([line[:line.index(' bags')] for line in relevant_lines]))
        new_colours = [ colour for colour in new_colours if colour not in colours_found]

        for colour in new_colours:
            colours_found.append(colour)
            containers = get_num_bags(colour)
            colours_found += containers

        colours_found = list(set(colours_found))
        return colours_found


colours = get_num_bags('shiny gold')
print(len(colours))
