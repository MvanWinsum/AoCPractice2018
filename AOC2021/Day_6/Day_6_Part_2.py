from collections import Counter

with open('puzzle_input.txt') as input_file:
    instruction_list = [input_line.strip().split(',') for input_line in input_file][0]
    instruction_list = [int(timer) for timer in instruction_list]
    fish_ages = {age:0 for age in range(0,9)}
    input_ages = dict(Counter(instruction_list))
    for age in input_ages.keys():
        fish_ages[age] = input_ages[age]
    print(fish_ages)


def simulate_day(pool):
    new_ages = {age:0 for age in range(0,9)}
    for age in pool.keys():
        new_age = age-1
        if new_age < 0:
            new_ages[8] += pool[age]
            new_ages[6] += pool[age]
        else:
            new_ages[new_age] += pool[age]
    return new_ages


for day_idx in range(256):
    fish_ages = simulate_day(fish_ages)

answer = 0
for age in fish_ages.keys():
    answer += fish_ages[age]
print(fish_ages)
print(answer)