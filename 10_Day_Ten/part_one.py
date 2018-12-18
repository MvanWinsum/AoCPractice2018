import pprint
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=4)
light_list = {}
grid_area = [[0, 0], [0, 0]]
area_list = []
scatter_list = [[], []]
index = 0
max_time = 20000
with open('puzzle_input.txt') as input_file:
    for input_line in input_file:
        input_line = input_line.strip().split(' ')
        light_list[index] = [input_line[0].split(','), input_line[1].split(',')]
        index += 1


def check_grid_area(grid, movement):
    if grid[0][0] > int(movement[0][0]):
        grid_area[0][0] = int(movement[0][0])
    if grid[0][1] < int(movement[0][0]):
        grid_area[0][1] = int(movement[0][0])
    if grid[1][0] > int(movement[0][1]):
        grid_area[1][0] = int(movement[0][1])
    if grid[1][1] < int(movement[0][1]):
        grid_area[1][1] = int(movement[0][1])


def apply_movement(movement, seconds_elapsed=1):
    check_grid_area(grid_area, movement)
    movement[0][0] = int(movement[0][0])
    movement[0][0] += int(movement[1][0]) * seconds_elapsed
    movement[0][1] = int(movement[0][1])
    movement[0][1] += int(movement[1][1]) * seconds_elapsed
    return movement


def calculate_grid_area(seconds_elapsed=1):
    move_second(seconds_elapsed)
    width = abs(grid_area[0][0]) + abs(grid_area[0][1])
    height = abs(grid_area[1][0]) + abs(grid_area[1][1])
    return int(width * height)


def move_second(seconds_elapsed=1):
    for light, movement in light_list.iteritems():
        light_list[light] = apply_movement(movement, seconds_elapsed)


# for second in range(0, max_time):
#     area_list.append(calculate_grid_area())
#     grid_area = [[0, 0], [0, 0]]
move_second(10454)
for light, movement in light_list.iteritems():
    scatter_list[0].append(movement[0][0])
    scatter_list[1].append(movement[0][1])
# lowest = 0
# lowest_index = 0
# index = 0
# for size in area_list:
#     if size < lowest or lowest == 0:
#         lowest = size
#         lowest_index = index
#     index += 1

plt.scatter(scatter_list[0], scatter_list[1])
plt.show()
# print(lowest_index)
