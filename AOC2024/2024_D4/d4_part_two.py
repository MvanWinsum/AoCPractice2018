mas_configurations = [
    'MSSM',
    'SSMM',
    'SMMS',
    'MMSS'
]

with open('puzzle_input.txt') as input_file:
    grid = [list(line.strip()) for line in input_file]

grid_width = len(grid[0])
grid_height = len(grid)

def check_mas(x_index:int, y_index:int):
    check_text = ''
    diagonal_positions = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
    for diagonal in diagonal_positions:
        check_text += grid[y_index + diagonal[0]][x_index + diagonal[1]]
    return True if check_text in mas_configurations else False

total_xmas_found = 0
for y_index in range(grid_height):
    for x_index in range(grid_width):
        if grid[y_index][x_index] == 'A':
            has_space_y = 0 < y_index < grid_height - 1
            has_space_x = 0 < x_index < grid_width - 1
            if has_space_x and has_space_y:
                total_xmas_found += 1 if check_mas(x_index, y_index) else 0

print(total_xmas_found)