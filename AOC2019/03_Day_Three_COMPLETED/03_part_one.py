def walk_steps(steps):
    x = 0
    y = 0
    crossed = []
    for step in steps:
        if step[0] == 'U':
            for take_step in range(int(step[1:])):
                y += 1
                crossed.append(tuple([x, y]))
        elif step[0] == 'D':
            for take_step in range(int(step[1:])):
                y -= 1
                crossed.append(tuple([x, y]))
        elif step[0] == 'R':
            for take_step in range(int(step[1:])):
                x += 1
                crossed.append(tuple([x, y]))
        elif step[0] == 'L':
            for take_step in range(int(step[1:])):
                x -= 1
                crossed.append(tuple([x, y]))
    return crossed


def check_intersections(wire_a, wire_b):
    return set(wire_a) & set(wire_b)


def closest_intersection(intersections):
    closest_distance = 0
    for intersection in intersections:
        intersection_distance = abs(intersection[0]) + abs(intersection[1])
        if closest_distance == 0 or closest_distance > intersection_distance:
            closest_distance = intersection_distance
    return closest_distance


with open('puzzle_input.txt') as input_file:
    wires = [x.replace("\n", "").split(',') for x in input_file.readlines()]
    wire_a = walk_steps(wires[0])
    wire_b = walk_steps(wires[1])
    intersections = check_intersections(wire_a, wire_b)
print(closest_intersection(intersections))
