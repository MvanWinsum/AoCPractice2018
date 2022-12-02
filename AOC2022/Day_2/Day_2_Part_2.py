with open('puzzle_input.txt') as input_file:
    move_collection = [line.strip().split(' ') for line in input_file]
    print(move_collection)


move_score = {
    'R': 1,
    'P': 2,
    'S': 3
}

move_translator = {
    'A': {
        'X': 'S',
        'Y': 'R',
        'Z': 'P'

    },
    'B': {
        'X': 'R',
        'Y': 'P',
        'Z': 'S'
    },
    'C': {
        'X': 'P',
        'Y': 'S',
        'Z': 'R'
    }
}

outcome_score = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

total_score = 0

for move in move_collection:
    my_move = move_translator[move[0]][move[1]]
    total_score += move_score[my_move]
    total_score += outcome_score[move[1]]
print(total_score)
