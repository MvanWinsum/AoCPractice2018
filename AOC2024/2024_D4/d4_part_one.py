search_word = 'XMAS'

with open('puzzle_input.txt') as input_file:
    grid = [list(line.strip()) for line in input_file]

grid_width = len(grid[0])
grid_height = len(grid)
print(grid)


def check_xmas_horizontal(x_index:int, y_index:int, reverse:bool = False):
    check_text = ''
    for letter_position in range(len(search_word)):
        x_position = x_index - letter_position if reverse else x_index + letter_position
        check_text += grid[y_index][x_position]
    return True if check_text == search_word else False

def check_xmas_vertical(x_index:int, y_index:int, reverse:bool = False):
    check_text = ''
    for letter_position in range(len(search_word)):
        y_position = y_index - letter_position if reverse else y_index + letter_position
        check_text += grid[y_position][x_index]
    return True if check_text == search_word else False

def check_xmas_diagonal(x_index:int, y_index:int, reverse_horizontal:bool = False, reverse_vertical:bool = False):
    check_text = ''
    for letter_position in range(len(search_word)):
        x_position = x_index - letter_position if reverse_horizontal else x_index + letter_position
        y_position = y_index - letter_position if reverse_vertical else y_index + letter_position
        check_text += grid[y_position][x_position]
    return True if check_text == search_word else False

def check_found_x(x_index:int, y_index:int):
    xmas_occurrences = 0
    has_space_right = x_index <= grid_width - len(search_word)
    has_space_left = x_index >= len(search_word) - 1
    has_space_bottom = y_index <= grid_height - len(search_word)
    has_space_top = y_index >= len(search_word) - 1
    if has_space_right:
        xmas_occurrences += 1 if check_xmas_horizontal(x_index, y_index) else 0
    if has_space_left:
        xmas_occurrences += 1 if check_xmas_horizontal(x_index, y_index, True) else 0
    if has_space_bottom:
        xmas_occurrences += 1 if check_xmas_vertical(x_index, y_index) else 0
    if has_space_top:
        xmas_occurrences += 1 if check_xmas_vertical(x_index, y_index, True) else 0
    if has_space_right and has_space_bottom:
        xmas_occurrences += 1 if check_xmas_diagonal(x_index, y_index) else 0
    if has_space_left and has_space_bottom:
        xmas_occurrences += 1 if check_xmas_diagonal(x_index, y_index, True) else 0
    if has_space_right and has_space_top:
        xmas_occurrences += 1 if check_xmas_diagonal(x_index, y_index, False, True) else 0
    if has_space_left and has_space_top:
        xmas_occurrences += 1 if check_xmas_diagonal(x_index, y_index, True, True) else 0

    return xmas_occurrences

total_xmas_found = 0
for y_index in range(grid_height):
    for x_index in range(grid_width):
        if grid[y_index][x_index] == 'X':
            total_xmas_found += check_found_x(x_index, y_index)

print(total_xmas_found)