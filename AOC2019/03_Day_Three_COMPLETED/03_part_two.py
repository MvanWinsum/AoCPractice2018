def walk_steps(steps):
    x = 0
    y = 0
    steps_done = 0
    crossed = {}
    for step in steps:
        if step[0] == 'U':
            for take_step in range(int(step[1:])):
                y += 1
                steps_done += 1
                crossed[(x, y)] = steps_done
        elif step[0] == 'D':
            for take_step in range(int(step[1:])):
                y -= 1
                steps_done += 1
                crossed[(x, y)] = steps_done
        elif step[0] == 'R':
            for take_step in range(int(step[1:])):
                x += 1
                steps_done += 1
                crossed[(x, y)] = steps_done
        elif step[0] == 'L':
            for take_step in range(int(step[1:])):
                x -= 1
                steps_done += 1
                crossed[(x, y)] = steps_done
    return crossed


with open('puzzle_input.txt') as input_file:
    wires = [x.replace("\n", "").split(',') for x in input_file.readlines()]
    wire_a = walk_steps(wires[0])
    wire_b = walk_steps(wires[1])
    intersections = set(wire_a.keys()) & set(wire_b.keys())
    least_steps = min([wire_a[p] + wire_b[p] for p in intersections])

print(least_steps)
