
with open('puzzle_input.txt') as input_file:
    list_one = []
    list_two = []
    for line in input_file:
        line = line.strip().split('   ')
        list_one.append(int(line[0]))
        list_two.append(int(line[1]))
    list_one.sort()
    list_two.sort()

total_difference = 0

for list_index in range(len(list_one)):
    total_difference += abs(list_one[list_index] - list_two[list_index])

print(total_difference)