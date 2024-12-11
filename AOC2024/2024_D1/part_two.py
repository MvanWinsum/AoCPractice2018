from collections import Counter

with open('puzzle_input.txt') as input_file:
    list_one = []
    list_two = []
    for line in input_file:
        line = line.strip().split('   ')
        list_one.append(int(line[0]))
        list_two.append(int(line[1]))
    list_two = Counter(list_two)

total_similarity = 0

for number in list_one:
    occurrences = list_two[number] if number in list_two else 0
    total_similarity += number * occurrences

print(total_similarity)