
with open('puzzle_input.txt') as input_file:
    reports = []
    for line in input_file:
        line = line.strip().split(' ')
        reports.append([int(number) for number in line])


def check_increasing_decreasing(list):
    check_list = list.copy()
    check_list.sort()
    if list == check_list:
        return True
    check_list.sort(reverse=True)
    if list == check_list:
        return True
    return False

def check_slowly_changing(list):
    eligible_deltas = [-3, -2, -1, 1, 2, 3]
    for list_idx in range(len(list) - 1):
        delta = list[list_idx+1] - list[list_idx]
        if delta not in eligible_deltas:
            return False
    return True

safe_reports = 0
for report in reports:
    if check_increasing_decreasing(report) and check_slowly_changing(report):
        safe_reports += 1

print(safe_reports)