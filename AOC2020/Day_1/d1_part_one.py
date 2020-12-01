with open('./puzzle_input.txt') as input_file:
    expenses = [int(expense_line) for expense_line in input_file]
    expenses.sort()

for index in range(len(expenses)):
    for index_reverse in range(len(expenses)):
        sum_of_expenses = expenses[index] + expenses[len(expenses) - index_reverse - 1]
        if sum_of_expenses == 2020:
            print('Answer: ' + str(expenses[index]) + ' - ' + str(expenses[len(expenses) - index_reverse - 1]))
            print('Puzzle_answer: %d' % (expenses[index] * expenses[len(expenses) - index_reverse - 1]))
        if sum_of_expenses < 2020:
            break