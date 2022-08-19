from collections import Counter
from pprint import PrettyPrinter

pp = PrettyPrinter(4)

with open('puzzle_input.txt') as input_file:
    path_collection = [path.strip().split('-') for path in input_file]
    print(path_collection)

caves_and_paths = {}
paths_to_end = []


def create_paths(source, destination):
    if source not in caves_and_paths and source != 'end':
        caves_and_paths[source] = []
    if destination not in caves_and_paths and destination != 'end':
        caves_and_paths[destination] = []
    if destination != 'start' and source != 'end':
        caves_and_paths[source].append(destination)


def explore_path(path_so_far, options):
    caves_visited = Counter(path_so_far.split('-'))
    for cave in caves_visited.keys():
        if cave.isupper():
            caves_visited[cave] = 0
    for option in options:
        if option == 'end':
            new_path = path_so_far + '-' + option
            paths_to_end.append(new_path)
            continue
        elif option.islower() and (option not in path_so_far.split('-') or (caves_visited[option] < 2 and 2 not in list(caves_visited.values()))):
            new_path = path_so_far + '-' + option
        elif option.isupper():
            new_path = path_so_far + '-' + option
        else:
            continue
        explore_path(new_path, caves_and_paths[option])


for path in path_collection:
    create_paths(path[0], path[1])
    create_paths(path[1], path[0])

print(caves_and_paths)

for start_option in caves_and_paths['start']:
    explore_path('start-' + start_option, caves_and_paths[start_option])


print(len(paths_to_end))