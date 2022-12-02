with open('puzzle_input.txt') as input_file:
    move_collection = [line.strip().split(' ') for line in input_file]
    print(move_collection)


move_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

outcome_scores = {
    'X': {
            'A': 3,
            'B': 0,
            'C': 6
         },
    'Y': {
            'A': 6,
            'B': 3,
            'C': 0
         },
    'Z': {
            'A': 0,
            'B': 6,
            'C': 3
         }
}

total_score = 0

for move in move_collection:
    total_score += move_score[move[1]]
    total_score += outcome_scores[move[1]][move[0]]
print(total_score)
