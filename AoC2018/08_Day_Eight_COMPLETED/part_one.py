import pprint
pp = pprint.PrettyPrinter(indent=4)
answer = 0
with open('puzzle_input.txt') as input_file:
    input_numbers = [input_line.strip().split(' ') for input_line in input_file]
    input_numbers = input_numbers[0]

def make_tree():
    tree = [0, 0, [], []]
    tree[0] = get_next_number()
    tree[1] = get_next_number()
    tree[2] = make_child_nodes(tree[0])
    tree[3] = add_metadata(tree[1])
    return tree


def get_next_number():
    global input_numbers
    if len(input_numbers) > 0:
        number = int(input_numbers.pop(0))
        return number
    return 0


def make_child_nodes(length):
    child_nodes = []
    for index in range(0, length):
        child_nodes.append(make_tree())
    return child_nodes


def add_metadata(length):
    global answer
    metadata = []
    for index in range(0, length):
        number = get_next_number()
        metadata.append(number)
        answer += number
    return metadata


full_tree = make_tree()
pp.pprint(full_tree)
pp.pprint(answer)