import json


class Monkey():
    def __init__(self, lines):
        self.index = lines[0][-2]
        self.items = [int(item) for item in lines[1].split(': ')[1].split(', ')]
        self.operation = list(lines[2].split(': ')[1].split(' '))
        self.test = int(lines[3].split(' ')[3])
        self.true = int(lines[4].split(' ')[5])
        self.false = int(lines[5].split(' ')[5])
        self.times_inspected = 0

    def perform_item_operation(self, item):
        if self.operation[4] == 'old':
            operate_by = item
        else:
            operate_by = int(self.operation[4])
        return int(eval(f'{item} {self.operation[3]} {operate_by}') / 3)

    def inspect_items(self):
        new_items = []
        for item in self.items:
            self.times_inspected += 1
            new_item = self.perform_item_operation(item)
            new_items.append(new_item)
        self.items = new_items

    def throw_item(self, item):
        indivisible = item % self.test
        self.items.remove(item)
        return self.true if not indivisible else self.false


with open('puzzle_input.txt') as input_file:
    operations = [line.strip() for line in input_file]

monkeys = []
monkey_lines = []
for operation in operations:
    monkey_lines.append(operation)
    if len(operation) == 0:
        new_monkey = Monkey(monkey_lines)
        monkeys.append(new_monkey)
        monkey_lines = []


for round in range(20):
    for monkey in monkeys:
        if len(monkey.items) > 0 :
            monkey.inspect_items()
            for item in monkey.items.copy():
                throw_to = monkey.throw_item(item)
                monkeys[throw_to].items.append(item)

for monkey in monkeys:
    print(f'Monkey {monkey.index} holds items {monkey.items} and divides by {monkey.test} and throws to {monkey.true} if true and to {monkey.false} if false and has inspected items {monkey.times_inspected} times')
