import pprint
import matplotlib.pyplot as plt
pp = pprint.PrettyPrinter(indent=4)
answer = 0
generations = 1000
previous_score = 0
score_deltas = []
scores = []
with open('initial_state.txt') as input_file:
    plant_state = [list(input_line) for input_line in input_file][0]

with open('transformations.txt') as transformation_file:
    transformations = {}
    for transformation_line in transformation_file:
        transformation = transformation_line.split(' => ')
        transformations[transformation[0].strip()] = transformation[1].strip()


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


def calculate_score(generation):
    global previous_score, current_score
    index = -2 * generation
    score = 0
    for plant in plant_state:
        if plant == '#':
            score += index
        index += 1
    score_delta = score - previous_score
    score_deltas.append(score_delta)
    scores.append(score)
    previous_score = score


for generation in range(generations):
    run_generation()
    calculate_score(generation)


plt.plot(scores)
plt.show()
