
with open('puzzle_input.txt') as input_file:
    tree_grid = [[int(number) for number in line.strip()] for line in input_file]
    print(tree_grid)


grid_size_x = len(tree_grid)
grid_size_y = len(tree_grid[0])

scenic_scores = []


def filter_scenic_trees(trees, height):
    filtered_trees = []
    for tree in trees:
        filtered_trees.append(tree)
        if tree >= height:
            break
    return filtered_trees


for x_coord in range(1, grid_size_x - 1):
    for y_coord in range(1, grid_size_y - 1):
        tree_height = tree_grid[x_coord][y_coord]
        scenic_trees =  {
            'left': filter_scenic_trees([tree_grid[x_coord][y_adjacent] for y_adjacent in range(0, y_coord)], tree_height),
            'right': filter_scenic_trees([tree_grid[x_coord][y_adjacent] for y_adjacent in range(y_coord + 1, grid_size_y)], tree_height),
            'up': filter_scenic_trees([tree_grid[x_adjacent][y_coord] for x_adjacent in range(0, x_coord)], tree_height),
            'down': filter_scenic_trees([tree_grid[x_adjacent][y_coord] for x_adjacent in range(x_coord, grid_size_x)], tree_height)
        }
        scenic_score = len(scenic_trees['up']) * len(scenic_trees['down']) * len(scenic_trees['left']) * len(scenic_trees['right'])
        scenic_scores.append(scenic_score)

print(max(scenic_scores))
