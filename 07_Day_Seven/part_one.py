import pprint, collections
pp = pprint.PrettyPrinter(indent=4)
parsed_workflow_entries = [[], []]
ready_for_execution = {}
need_prerequisite = {}
action_flow = ''
with open('puzzle_input.txt') as input_file:
    workflow_entries = [input_line.strip() for input_line in input_file]


def parse_input_to_workflow_entries():
    for entry in workflow_entries:
        entry = entry.split(' ')
        parsed_workflow_entries[0].append(entry[0].strip())
        parsed_workflow_entries[1].append(entry[1].strip())


def filter_prerequisite_actions(entries):
    global ready_for_execution
    global need_prerequisite
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


def execute_action(action_to_execute):
    global action_flow, need_prerequisite, ready_for_execution
    action_flow += action_to_execute
    del ready_for_execution[action_to_execute]
    for action, prerequisites in need_prerequisite.iteritems():
        if action_to_execute in prerequisites:
            del prerequisites[action_to_execute]
        if len(prerequisites) == 0:
            ready_for_execution[action] = action
            del need_prerequisite[action]
    ready_for_execution = collections.OrderedDict(sorted(ready_for_execution.items()))
    need_prerequisite = collections.OrderedDict(sorted(need_prerequisite.items()))


# Main Script Functionality
parse_input_to_workflow_entries()
filter_prerequisite_actions(parsed_workflow_entries)
pp.pprint(need_prerequisite)
while len(ready_for_execution) > 0:
    action_to_execute = next(iter(ready_for_execution))
    execute_action(action_to_execute)
pp.pprint(action_flow)
