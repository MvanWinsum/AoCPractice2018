max_recipe_steps = 824501
recipe_list = [3, 7]
elf_one_index = 0
elf_two_index = 1


def calculate_new_scores(elf_one_score, elf_two_score):
    score_sum = [int(digit) for digit in list(str(elf_one_score + elf_two_score))]
    recipe_list.extend(score_sum)


def get_new_indices_for_elves():
    global elf_one_index, elf_two_index
    elf_one_index = (elf_one_index + 1 + recipe_list[elf_one_index]) % len(recipe_list)
    elf_two_index = (elf_two_index + 1 + recipe_list[elf_two_index]) % len(recipe_list)


for generation in range(max_recipe_steps + 10):
    calculate_new_scores(recipe_list[elf_one_index], recipe_list[elf_two_index])
    get_new_indices_for_elves()

print(''.join(str(score) for score in recipe_list[max_recipe_steps:max_recipe_steps+10]))
