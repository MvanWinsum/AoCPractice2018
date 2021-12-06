import pprint as pp
printer = pp.PrettyPrinter(indent=4)

with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip() for input_line in input_file]
    drawn_numbers = instruction_list[0].split(',')
    del instruction_list[0]
    # grid = grid[grid_number][grid_y][grid_x]
    grids = []
    current_board = []
    for line in instruction_list:
        if line == '':
            grids.append(current_board)
            current_board = []
        else:
            current_board.append(line.split(' '))
    grids.append(current_board)
    # pp.pprint(grids)


def check_board(board, number):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] != 'X' and int(board[row][column]) == int(number):
                return [row,column]
    return False


def check_horizontal(board):
    for row in board:
        if len(set(row)) == 1 and row[0] == 'X':
            return True


def check_vertical(board):
    for column in range(len(board[0])):
        column_marked = True
        for row in range(len(board)):
            if board[row][column] != 'X':
                column_marked = False
                break
        if column_marked:
            return column_marked
    return False


def add_unmarked(board):
    total = 0
    for row in board:
        for number in row:
            if number != 'X':
                total += int(number)
    return total


number_found = False
for number in drawn_numbers:
    board_index = 0
    to_delete = []
    for board in grids:
        mark_number = check_board(board, number)
        if mark_number:
            board[mark_number[0]][mark_number[1]] = 'X'
        if check_vertical(board) or check_horizontal(board):
            if len(grids) == 1:
                total_unmarked = add_unmarked(board)
                print(f"Board: {board} \n Drawn number: {number} \n Total unmarked: {total_unmarked}")
                number_found = True
            else:
                to_delete.append(board_index)
        board_index += 1
    to_delete.sort(reverse=True)
    for delete_index in to_delete:
        del grids[delete_index]
    if number_found:
        break
