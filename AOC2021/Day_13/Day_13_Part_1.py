from pprint import PrettyPrinter

pp = PrettyPrinter(4)

with open('puzzle_input_dots.txt') as input_file:
    dot_collection = [[int(coordinate) for coordinate in path.strip().split(',')] for path in input_file]
    print(dot_collection)

with open('puzzle_input_folds.txt') as input_file:
    fold_collection = [path.strip().split(' ')[2].split('=') for path in input_file]
    print(fold_collection)


def find_grid_sizes(grid):
    highest_x = 0
    highest_y = 0
    for dot in grid:
        if dot[0] > highest_x:
            highest_x = dot[0]
        if dot[1] > highest_y:
            highest_y = dot[1]
    return [highest_x, highest_y]


def fold_dot_y(dot, fold_line):
    distance_to_fold = dot[0] - fold_line
    if distance_to_fold >= 0:
        new_dot = [fold_line - distance_to_fold, dot[1]]
        return new_dot
    return dot


def fold_dot_x(dot, fold_line, grid_width):
    distance_to_fold = fold_line - dot[1]
    if distance_to_fold >= 0:
        new_dot = [dot[0], fold_line + distance_to_fold]
        return new_dot
    return dot

pp.pprint(dot_collection)

for fold in fold_collection:
    grid_dimensions = find_grid_sizes(dot_collection)
    grid_after_fold = []
    if fold[0] == 'y':
        for dot in dot_collection:
            new_dot = fold_dot_y(dot, int(fold[1]))
            if new_dot not in grid_after_fold:
                grid_after_fold.append(new_dot)
    elif fold[0] == 'x':
        for dot in dot_collection:
            new_dot = fold_dot_x(dot, int(fold[1]))
            if new_dot not in grid_after_fold:
                grid_after_fold.append(new_dot)
    print(len(grid_after_fold))
    dot_collection = grid_after_fold
    break

print(find_grid_sizes(dot_collection))