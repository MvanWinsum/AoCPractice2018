with open('puzzle_input.txt') as input_file:
    assignment_collection = [[assignment.split('-') for assignment in line.strip().split(',')] for line in input_file]


redundant_assignments = []
for assignment in assignment_collection:
    if len(list(set(range(int(assignment[0][0]), int(assignment[0][1]) + 1)) & set(range(int(assignment[1][0]), int(assignment[1][1]) + 1)))) > 0:
        redundant_assignments.append(assignment)
print(len(redundant_assignments))