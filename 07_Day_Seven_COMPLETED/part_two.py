import pprint, collections
pp = pprint.PrettyPrinter(indent=4)
with open('puzzle_input.txt') as input_file:
    input_letters = [input_line.strip() for input_line in input_file][0]
pp = pprint.PrettyPrinter(indent=4)
seconds_elapsed = 0
parsed_workflow_entries = [[], []]
workers = {'0': '', '1': '', '2': '', '3': '', '4': ''}
letter_indices = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
ready_for_execution = {}
need_prerequisite = {}
operations_in_progress = {}
operation_flow = str('')
with open('puzzle_input.txt') as input_file:
    workflow_entries = [input_line.strip() for input_line in input_file]


def parse_input_to_workflow_entries():
    for entry in workflow_entries:
        entry = entry.split(' ')
        parsed_workflow_entries[0].append(entry[0].strip())
        parsed_workflow_entries[1].append(entry[1].strip())


def filter_prerequisite_actions(entries):
    global ready_for_execution, need_prerequisite
    index = 0
    for entry in entries[0]:
        if entry not in entries[1]:
            ready_for_execution[entry] = [entry]
        if entries[1][index] not in need_prerequisite:
            need_prerequisite[entries[1][index]] = {entry: entry}
        else:
            need_prerequisite[entries[1][index]][entry] = entry
        index += 1
    ready_for_execution = collections.OrderedDict(sorted(ready_for_execution.items()))
    need_prerequisite = collections.OrderedDict(sorted(need_prerequisite.items()))


def finish_action_in_progress(action_to_execute):
    global operation_flow, need_prerequisite, ready_for_execution
    for action, prerequisites in need_prerequisite.iteritems():
        if action_to_execute in prerequisites:
            del prerequisites[action_to_execute]
        if len(prerequisites) == 0:
            ready_for_execution[action] = action
            del need_prerequisite[action]
    del operations_in_progress[action_to_execute]
    operation_flow += action_to_execute
    ready_for_execution = collections.OrderedDict(sorted(ready_for_execution.items()))
    need_prerequisite = collections.OrderedDict(sorted(need_prerequisite.items()))


# Main Script Functionality
parse_input_to_workflow_entries()
filter_prerequisite_actions(parsed_workflow_entries)
pp.pprint(ready_for_execution)
pp.pprint('Workflow Log Advent of Code 2018:')
pp.pprint('[--Sc--W1--W2--W3--W4--W5--Flow----------------------]')
while len(operation_flow) < 26:
    for worker, operation in workers.iteritems():
        if len(workers[worker]) > 0:
            operations_in_progress[workers[worker]] -= 1
            if operations_in_progress[workers[worker]] < 1:
                finish_action_in_progress(workers[worker])
                workers[worker] = ''
        if operation == '' and len(ready_for_execution.items()) > 0:
            operation_to_execute = next(iter(ready_for_execution))
            operations_in_progress[operation_to_execute] = 60 + letter_indices[operation_to_execute]
            workers[worker] = operation_to_execute
            del ready_for_execution[operation_to_execute]
    pp.pprint('|  ' + str(seconds_elapsed) + '  ' + workers['0'] + '  ' + workers['1'] + '  ' + workers['2'] + '  ' + workers['3'] + '  ' + workers['4'] + ' | ' + str(operation_flow) + ' ]')
    seconds_elapsed += 1
pp.pprint('[--Sc--W1--W2--W3--W4--W5--Flow-----------------------]')
pp.pprint(operation_flow)

#
# execute_action(action_to_execute)