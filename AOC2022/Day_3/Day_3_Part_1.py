with open('puzzle_input.txt') as input_file:
    backpack_collection = [list(line.strip()) for line in input_file]

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
split_backpacks = []
total_score = 0
for backpack in backpack_collection:
    split_index = int(len(backpack) / 2)
    shared_letter = list(set(backpack[:split_index]) & set(backpack[split_index:]))[0]
    total_score += letters.index(shared_letter) + 1

print(total_score)