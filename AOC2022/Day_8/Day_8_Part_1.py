
with open('puzzle_input.txt') as input_file:
    tree_grid = [[int(number) for number in line.strip()] for line in input_file]
    print(tree_grid)


grid_size_x = len(tree_grid)
grid_size_y = len(tree_grid[0])

visible_trees = []


for x_coord in range(grid_size_x):
    for y_coord in range(grid_size_y):
        tree_height = tree_grid[x_coord][y_coord]
        if x_coord == 0 or x_coord == grid_size_x - 1 or y_coord == 0 or y_coord == grid_size_y - 1:
            visible_trees.append([x_coord, y_coord])
        elif tree_height > max([tree_grid[x_coord][y_adjacent] for y_adjacent in range(0,y_coord)]):
            visible_trees.append([x_coord, y_coord])
        elif tree_height > max([tree_grid[x_coord][y_adjacent] for y_adjacent in range(y_coord+1, grid_size_y)]):
            visible_trees.append([x_coord, y_coord])
        elif tree_height > max([tree_grid[x_adjacent][y_coord] for x_adjacent in range(0, x_coord)]):
            visible_trees.append([x_coord, y_coord])
        elif tree_height > max([tree_grid[x_adjacent][y_coord] for x_adjacent in range(x_coord+1, grid_size_x)]):
            visible_trees.append([x_coord, y_coord])

print(len(visible_trees))