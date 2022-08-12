from pprint import pprint

with open('puzzle_input.txt') as input_file:
    octopus_grid = [[int(number) for number in input_line.strip()] for input_line in input_file]

flashes_this_round = []
has_flashed = []
number_of_flashes = 0


def reset_flashed_octopodes(grid):
    for coordinate_y in range(len(grid)):
        for coordinate_x in range(len(grid[0])):
            if grid[coordinate_y][coordinate_x] > 9:
                grid[coordinate_y][coordinate_x] = 0
    return grid


def increment_all_octopodes(grid):
    for coordinate_y in range(len(grid)):
        for coordinate_x in range(len(grid[0])):
            grid[coordinate_y][coordinate_x] += 1
            if grid[coordinate_y][coordinate_x] > 9 and [coordinate_y, coordinate_x] not in flashes_this_round:
                flashes_this_round.append([coordinate_y, coordinate_x])
    return grid


def increment_adjacent_octopodes(grid, coordinates):
    delta_y = [-1, 0, 1]
    delta_x = [-1, 0, 1]
    for y in delta_y:
        for x in delta_x:
            if x == 0 and y == 0:
                continue
            else:
                coordinate_y = coordinates[0] + y
                coordinate_x = coordinates[1] + x
                if coordinate_y in range(len(grid)) and coordinate_x in range(len(grid[0])):
                    grid[coordinate_y][coordinate_x] += 1
                    if grid[coordinate_y][coordinate_x] > 9 and [coordinate_y, coordinate_x] not in flashes_this_round:
                        flashes_this_round.append([coordinate_y, coordinate_x])
    return grid


for round in range(100):
    flashes_this_round = []
    has_flashed = []
    octopus_grid = increment_all_octopodes(octopus_grid)
    while len(flashes_this_round) > len(has_flashed):
        octopus_grid = increment_adjacent_octopodes(
            octopus_grid,
            flashes_this_round[len(has_flashed)]
        )
        has_flashed.append(flashes_this_round[len(has_flashed)])
    number_of_flashes += len(flashes_this_round)
    octopus_grid = reset_flashed_octopodes(octopus_grid)
print(number_of_flashes)
