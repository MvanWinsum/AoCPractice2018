import pprint
pp = pprint.PrettyPrinter(indent=4)
answer = 0
generations = 50000000000
with open('initial_state.txt') as input_file:
    plant_state = [list(input_line) for input_line in input_file][0]

with open('transformations.txt') as transformation_file:
    transformations = {}
    for transformation_line in transformation_file:
        transformation = transformation_line.split(' => ')
        transformations[transformation[0].strip()] = transformation[1].strip()


def get_plant_at_index(index):
    if index < 0 or index > len(plant_state) - 1:
        return '.'
    return plant_state[index]


def get_plant_configuration(index):
    return get_plant_at_index(index - 2) + \
           get_plant_at_index(index - 1) + \
           get_plant_at_index(index) + \
           get_plant_at_index(index + 1) + \
           get_plant_at_index(index + 2)


def run_generation():
    global plant_state
    plant_state = ['.', '.'] + plant_state
    plant_state.extend(['.', '.'])
    read_state = ['.', '.'] + plant_state
    read_state.extend(['.', '.'])
    new_plant_state = []
    for i in range(len(plant_state)):
        pat = ''.join(read_state[i:i + 5])
        new_plant_state.append(transformations.get(pat, '.'))
    plant_state = new_plant_state


for generation in range(generations):
    print(''.join(plant_state))
    run_generation()

index = -2 * generations
score = 0
for plant in plant_state:
    if plant == '#':
        score += index
    index += 1
print(score)


