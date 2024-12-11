import re

with open('puzzle_input.txt') as input_file:
    instructions = ''
    for line in input_file:
        line = line.strip()
        instructions += line


def find_closest_do_dont(match, do_matches):
    match_start_index = match.start()
    closest_do_dont = None
    for do_match in do_matches:
        if do_match.start() < match_start_index:
            closest_do_dont = do_match
        else:
            break
    return closest_do_dont


mul_regex = r"mul\((\d+),(\d+)\)"
matched_mul = re.finditer(mul_regex, instructions)
total_sum = 0

do_regex = r"do\(\)|don't\(\)"
do_matches = re.finditer(do_regex, instructions)
do_matches = [match for match in do_matches]


for match in matched_mul:
    closest_do = find_closest_do_dont(match, do_matches)
    if closest_do is not None and closest_do.group(0).find('don') > -1:
        continue
    total_sum += int(match.group(1)) * int(match.group(2))

print(total_sum)