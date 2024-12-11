
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

def check_report_safe(report):
    if check_increasing_decreasing(report) and check_slowly_changing(report):
        return True
    return False

safe_reports = 0
for report in reports:
    full_report_check = check_report_safe(report)
    if full_report_check:
        safe_reports += 1
    else:
        for check_idx in range(len(report)):
            check_error_report = report.copy()
            del check_error_report[check_idx]
            if check_report_safe(check_error_report):
                safe_reports += 1
                break

print(safe_reports)