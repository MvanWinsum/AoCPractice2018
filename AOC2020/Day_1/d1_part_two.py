with open('./puzzle_input.txt') as input_file:
    expenses = [int(expense_line) for expense_line in input_file]
    expenses.sort()

for index in range(len(expenses)):
    for index_reverse in range(len(expenses)):
        sum_of_expenses = expenses[index] + expenses[len(expenses) - index_reverse - 1]
        if 2020 - sum_of_expenses in expenses:
            print('Answer: %d - %d - %d' %
                  (expenses[index], expenses[len(expenses) - index_reverse - 1], 2020 - sum_of_expenses))
            print('Puzzle_answer: %d' %
                  (expenses[index] * expenses[len(expenses) - index_reverse - 1] * 2020 - sum_of_expenses))
