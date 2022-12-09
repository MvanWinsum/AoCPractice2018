
with open('puzzle_input.txt') as input_file:
    movements = [line.strip().split(' ') for line in input_file]


current_knot_positions = [[0, 0] for tail in range(10)]


def move_head(current_knot_position, direction):
    direction_movement = {
        'R': [1, 0],
        'L': [-1, 0],
        'U': [0, -1],
        'D': [0, 1]
    }
    current_knot_position[0] += direction_movement[direction][0]
    current_knot_position[1] += direction_movement[direction][1]
    return current_knot_position


def follow_head(current_knot_position, previous_knot_position):
    head_to_tail_distance = [
        previous_knot_position[0] - current_knot_position[0],
        previous_knot_position[1] - current_knot_position[1]
    ]
    match head_to_tail_distance:
        case [2, 0]: current_knot_position = [current_knot_position[0] + 1, current_knot_position[1]]
        case [0, 2]: current_knot_position = [current_knot_position[0], current_knot_position[1] + 1]
        case [-2, 0]: current_knot_position = [current_knot_position[0] - 1, current_knot_position[1]]
        case [0, -2]: current_knot_position = [current_knot_position[0], current_knot_position[1] - 1]
        case [2, 1]: current_knot_position = [current_knot_position[0] + 1, current_knot_position[1] + 1]
        case [1, 2]: current_knot_position = [current_knot_position[0] + 1, current_knot_position[1] + 1]
        case [-1, -2]: current_knot_position = [current_knot_position[0] - 1, current_knot_position[1] - 1]
        case [1, -2]: current_knot_position = [current_knot_position[0] + 1, current_knot_position[1] - 1]
        case [-1, 2]: current_knot_position = [current_knot_position[0] - 1, current_knot_position[1] + 1]
        case [-2, 1]: current_knot_position = [current_knot_position[0] - 1, current_knot_position[1] + 1]
        case [-2, -1]: current_knot_position = [current_knot_position[0] - 1, current_knot_position[1] - 1]
        case [2, -1]: current_knot_position = [current_knot_position[0] + 1, current_knot_position[1] - 1]
        case [2, -2]: current_knot_position = [current_knot_position[0] + 1, current_knot_position[1] - 1]
        case [-2, -2]: current_knot_position = [current_knot_position[0] - 1, current_knot_position[1] - 1]
        case [2, 2]: current_knot_position = [current_knot_position[0] + 1, current_knot_position[1] + 1]
        case [-2, 2]: current_knot_position = [current_knot_position[0] - 1, current_knot_position[1] + 1]
    return current_knot_position


unique_tail_positions = []

for movement in movements:
    for movement_idx in range(int(movement[1])):
        current_knot_positions[0] = move_head(current_knot_positions[0], movement[0])
        for knot_idx in range(1, len(current_knot_positions)):
            current_knot_positions[knot_idx] = follow_head(current_knot_positions[knot_idx], current_knot_positions[knot_idx - 1])
        if current_knot_positions[-1] not in unique_tail_positions:
            unique_tail_positions.append(current_knot_positions[-1])

print(len(unique_tail_positions))
