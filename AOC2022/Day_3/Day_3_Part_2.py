
with open('puzzle_input.txt') as input_file:
    backpack_collection = [list(line.strip()) for line in input_file]

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
split_backpacks = []
total_score = 0
index = 2

while index <= len(backpack_collection):
    shared_letter = list(set(backpack_collection[index]) & set(backpack_collection[index-1]) & set(backpack_collection[index-2]))[0]
    total_score += letters.index(shared_letter) + 1
    index += 3

print(total_score)
