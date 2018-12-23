import pprint
pp = pprint.PrettyPrinter()
grid_serial_number = 3999
grid = {}
highest_power = 0
highest_coord = ''

def calculate_power_level(x_coord, y_coord):
    rack_id = int(x_coord) + 10
    power_level = (rack_id * int(y_coord) + grid_serial_number) * rack_id
    hundreds = power_level % 1000
    if hundreds < 100:
        return 0
    else:
        return int(str(hundreds)[0]) - 5


def create_grid(max_x, max_y):
    global grid
    for x in range(1, max_x):
        for y in range(1, max_y):
            grid[str(x) + ',' + str(y)] = 0


def calculate_grid_level():
    for coord, score in grid.iteritems():
        coord_pair = coord.split(',')
        grid[coord] = calculate_power_level(coord_pair[0], coord_pair[1])


def get_square_score(position):
    coordinates = position.split(',')
    square_score = 0
    for x in range(int(coordinates[0]), int(coordinates[0]) + 3):
        for y in range(int(coordinates[1]), int(coordinates[1]) + 3):
            if str(x) + ',' + str(y) in grid:
                square_score += grid[str(x) + ',' + str(y)]
            else:
                return 0
    return square_score


def get_highest_square():
    global highest_power, highest_coord, grid
    for coord, score in grid.iteritems():
        square_score = get_square_score(coord)
        if square_score > highest_power:
            highest_power = square_score
            highest_coord = coord


create_grid(300, 300)
calculate_grid_level()
get_highest_square()
pp.pprint(highest_power)
pp.pprint(highest_coord)