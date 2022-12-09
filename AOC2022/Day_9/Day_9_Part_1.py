
with open('puzzle_input.txt') as input_file:
    movements = [line.strip().split(' ') for line in input_file]


current_head_position = [0, 0]
current_tail_position = [0, 0]


def move_head(direction):
    direction_movement = {
        'R': [1, 0],
        'L': [-1, 0],
        'U': [0, -1],
        'D': [0, 1]
    }
    current_head_position[0] += direction_movement[direction][0]
    current_head_position[1] += direction_movement[direction][1]


def follow_head(current_tail_position):
    head_to_tail_distance = [
        current_head_position[0] - current_tail_position[0],
        current_head_position[1] - current_tail_position[1]
    ]
    match head_to_tail_distance:
        case [2, 0]: current_tail_position = [current_tail_position[0] + 1, current_tail_position[1]]
        case [0, 2]: current_tail_position = [current_tail_position[0], current_tail_position[1] + 1]
        case [-2, 0]: current_tail_position = [current_tail_position[0] - 1, current_tail_position[1]]
        case [0, -2]: current_tail_position = [current_tail_position[0], current_tail_position[1] - 1]
        case [2, 1]: current_tail_position = [current_tail_position[0] + 1, current_tail_position[1] + 1]
        case [1, 2]: current_tail_position = [current_tail_position[0] + 1, current_tail_position[1] + 1]
        case [-1, -2]: current_tail_position = [current_tail_position[0] - 1, current_tail_position[1] - 1]
        case [1, -2]: current_tail_position = [current_tail_position[0] + 1, current_tail_position[1] - 1]
        case [-1, 2]: current_tail_position = [current_tail_position[0] - 1, current_tail_position[1] + 1]
        case [-2, 1]: current_tail_position = [current_tail_position[0] - 1, current_tail_position[1] + 1]
        case [-2, -1]: current_tail_position = [current_tail_position[0] - 1, current_tail_position[1] - 1]
        case [2, -1]: current_tail_position = [current_tail_position[0] + 1, current_tail_position[1] - 1]
    return current_tail_position


unique_tail_positions = []

for movement in movements:
    for movement_idx in range(int(movement[1])):
        move_head(movement[0])
        current_tail_position = follow_head(current_tail_position)
        if current_tail_position not in unique_tail_positions:
            unique_tail_positions.append(current_tail_position)

print(len(unique_tail_positions))
