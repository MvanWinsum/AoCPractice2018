slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
trees_encountered = []

# Reading and parsing input
with open('./puzzle_input.txt') as input_file:
    tree_lines = [line.strip() for line in input_file]
    print(tree_lines)

for slope in slopes:
    slope_trees = 0
    position_X = 0
    position_Y = 0
    while position_Y + 1 < len(tree_lines):
        position_X = (position_X + slope[0]) % len(tree_lines[0])
        position_Y += slope[1]
        if tree_lines[position_Y][position_X] == '#':
            slope_trees += 1
    trees_encountered.append(slope_trees)

print(trees_encountered)