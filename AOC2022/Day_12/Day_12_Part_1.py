
with open('puzzle_input.txt') as input_file:
    grid = [list(line.strip()) for line in input_file]
    print(grid)

elevation = 'SabcdefghijklmnopqrstuvwxyzE'
shortest_route = 9999
viable_routes = []

def find_start_end_position(grid):
    start = [0, 0]
    end = [0, 0]
    for x_coord in range(len(grid[0])):
        for y_coord in range(len(grid)):
            if grid[y_coord][x_coord] == 'S':
                start = [y_coord, x_coord]
            elif grid[y_coord][x_coord] == 'E':
                end = [y_coord, x_coord]
    return start, end


def walk_route(position, route, grid, shortest_route=None):
    # Stop if further exploration is useless
    if len(route) >= shortest_route:
        return
    # Stop if we reached the endzone
    if grid[position[0]][position[1]] == 'E':
        viable_routes.append(route)
        shortest_route = len(route)
        print(f'Shortest route: {shortest_route} steps')
    current_elevation = elevation.index(grid[position[0]][position[1]])
    possible_steps = []
    # up
    if position[0] > 0:
        new_position = [position[0]-1,position[1]]
        if elevation.index(grid[position[0]-1][position[1]]) <= current_elevation + 1:
            possible_steps.append(new_position)
    #down
    if position[0] < len(grid) - 1:
        new_position = [position[0]+1,position[1]]
        if elevation.index(grid[position[0]+1][position[1]]) <= current_elevation + 1:
            possible_steps.append(new_position)
    #left
    if position[1] > 0:
        new_position = [position[0]+1,position[1]]
        if elevation.index(grid[position[0]][position[1]-1]) <= current_elevation + 1:
            possible_steps.append(new_position)
    #right
    if position[1] < len(grid[0]) - 1:
        new_position = [position[0]+1,position[1]]
        if elevation.index(grid[position[0]][position[1]+1]) <= current_elevation + 1:
            possible_steps.append(new_position)
    print(possible_steps)
    possible_steps = sorted(possible_steps, key=lambda x: abs((end_point[0] - int(x[0])) + (end_point[1] - int(x[1]))))
    print(possible_steps)
    for step in possible_steps:
        walk_route(step, route + step, grid, shortest_route)


start_point, end_point = find_start_end_position(grid)
walk_route(start_point, [[0, 0]], grid, shortest_route)
print(f'Start: {start_point} End: {end_point}')
print(f'Routes: {viable_routes}')









