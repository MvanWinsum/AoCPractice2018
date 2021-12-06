import pprint as pp
printer = pp.PrettyPrinter(indent=4)

with open('puzzle_input.txt') as input_file:
    instruction_list = []
    for input_line in input_file:
        input_line = input_line.strip().split(' -> ')
        input_line[0] = input_line[0].split(',')
        input_line[1] = input_line[1].split(',')
        if input_line[0][0] == input_line[1][0] or input_line[0][1] == input_line[1][1]:
            instruction_list.append(input_line)


def get_grid_dimensions(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        if int(line[0][0]) > max_x:
            max_x = int(line[0][0])
        if int(line[1][0]) > max_x:
            max_x = int(line[1][0])
        if int(line[0][1]) > max_y:
            max_y = int(line[0][1])
        if int(line[1][1]) > max_y:
            max_y = int(line[1][1])
    return max_x+1, max_y+1


def create_grid(x,y):
    grid = []
    for row in range(y):
        grid.append([])
        for column in range(x):
            grid[row].append(0)
    return grid


def draw_line(grid, line):
    x_line = [int(line[0][0]), int(line[1][0])]
    if x_line[0] == x_line[1]:
        x_line = [x_line[0]]
    else:
        x_line.sort()
        x_line = range(x_line[0], x_line[1]+1)
    y_line = [int(line[0][1]), int(line[1][1])]
    if y_line[0] == y_line[1]:
        y_line = [y_line[0]]
    else:
        y_line.sort()
        y_line = range(y_line[0], y_line[1]+1)
    for x_coord in x_line:
        for y_coord in y_line:
            grid[y_coord][x_coord] += 1
    return grid


def get_answer(grid):
    more_than_two = 0
    for row in grid:
        for column in row:
            if column > 1:
                more_than_two += 1
    return more_than_two


grid_x, grid_y = get_grid_dimensions(instruction_list)
grid = create_grid(grid_x, grid_y)
for line in instruction_list:
    grid = draw_line(grid, line)

print(get_answer(grid))