
with open('puzzle_input.txt') as input_file:
    instruction_list = [[int(number) for number in input_line.strip()] for input_line in input_file]
    print(instruction_list)

answer = 0

for row_idx in range(0, len(instruction_list)):
    for column_idx in range(0, len(instruction_list[0])):
        eligible_number = True
        adjacents = []
        if row_idx > 0:
            # check value above
            adjacents.append(instruction_list[row_idx-1][column_idx])
            if instruction_list[row_idx][column_idx] >= instruction_list[row_idx-1][column_idx]:
                eligible_number = False
        if row_idx < len(instruction_list)-1:
            # check row below
            adjacents.append(instruction_list[row_idx+1][column_idx])
            if instruction_list[row_idx][column_idx] >= instruction_list[row_idx+1][column_idx]:
                eligible_number = False
        if column_idx > 0:
            # check value left
            adjacents.append(instruction_list[row_idx][column_idx-1])
            if instruction_list[row_idx][column_idx] >= instruction_list[row_idx][column_idx-1]:
                eligible_number = False
        if column_idx < len(instruction_list[0])-1:
            #check value right
            adjacents.append(instruction_list[row_idx][column_idx+1])
            if instruction_list[row_idx][column_idx] >= instruction_list[row_idx][column_idx+1]:
                eligible_number = False
        if eligible_number:
            print(f'Eligible number! Number: {instruction_list[row_idx][column_idx]} adjacents: {adjacents}')
            answer += 1+instruction_list[row_idx][column_idx]

print(answer)