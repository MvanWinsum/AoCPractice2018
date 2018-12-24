from collections import deque
import collections
import pprint

pp = pprint.PrettyPrinter(indent=4)
actions = deque(['L', 'S', 'R'])
curves = {}
intersections = {}
carts = {}
first_crash = ''

with open('input.txt') as input_file:
    grid = [input_line.replace('\n', '') for input_line in input_file]


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def parse_grid_line(grid_line, grid_index):
    # Parse Curves
    for curve in find(grid_line, '/'):
        curves[grid_index] = {curve : '/'}
    for curve in find(grid_line, '\\'):
        curves[grid_index] = {curve : '\\'}
    # Parse Intersections
    for intersection in find(grid_line, '+'):
        intersections[grid_index] = {intersection: '+'}
    # Parse Carts
    for cart in find(grid_line, '>'):
        carts[grid_index] = {cart: ['R', actions]}
    for cart in find(grid_line, '<'):
        carts[grid_index] = {cart: ['L', actions]}
    for cart in find(grid_line, '^'):
        carts[grid_index] = {cart: ['U', actions]}
    for cart in find(grid_line, 'V'):
        carts[grid_index] = {cart: ['D', actions]}


def sort_carts():
    global carts
    carts = collections.OrderedDict(sorted(carts.items()))


def parse_grid():
    index = 0
    for line in grid:
        parse_grid_line(line, index)
        index += 1
    sort_carts()


def adjust_movement_curve(movement, curve):
    if curve == '/':
        if movement == 'R':
            return 'D'
        if movement == 'D':
            return 'L'
        if movement == 'U':
            return 'R'
        if movement == 'L':
            return 'U'
    else:
        if movement == 'R':
            return 'U'
        if movement == 'D':
            return 'R'
        if movement == 'U':
            return 'L'
        if movement == 'L':
            return 'D'


def adjust_movement_intersection(cart):
    movement, queue = cart[0], cart[1]
    if movement == 'L':
        if queue[0] == 'L':
            cart[0] = 'D'
        if queue[0] == 'R':
            cart[0] = 'U'
    if movement == 'R':
        if queue[0] == 'L':
            cart[0] = 'U'
        if queue[0] == 'R':
            cart[0] = 'D'
    if movement == 'U':
        if queue[0] == 'L':
            cart[0] = 'L'
        if queue[0] == 'R':
            cart[0] = 'R'
    if movement == 'D':
        if queue[0] == 'L':
            cart[0] = 'R'
        if queue[0] == 'R':
            cart[0] = 'L'
    cart[1] = queue.rotate(-1)
    return cart


def get_new_cart_coordinates(cart, current_y, current_x):
    if cart[0] == 'L':
        moved_y, moved_x = current_y, current_x - 1
    if cart[0] == 'R':
        moved_y, moved_x = current_y, current_x + 1
    if cart[0] == 'U':
        moved_y, moved_x = current_y - 1, current_x
    if cart[0] == 'D':
        moved_y, moved_x = current_y + 1, current_x
    return moved_y, moved_x


def run_tick():
    global first_crash, carts
    ticked_carts = {}
    for y, xcart in carts.iteritems():
        for x, cart in xcart.iteritems():
            if y in curves and x in curves[y]:
                carts[y][x][0] = adjust_movement_curve(cart[0], curves[y][x])
            if y in intersections and x in intersections[y]:
                carts[y][x] = adjust_movement_intersection(cart)
            new_y, new_x = get_new_cart_coordinates(carts[y][x], y, x)
            if new_y in carts and new_x in carts[y]:
                first_crash = str(new_x) + ',' + str(new_y)
                return
            ticked_carts[new_y] = {new_x: cart}
    carts = ticked_carts


parse_grid()
while len(first_crash) == 0:
    run_tick()
    sort_carts()
pp.pprint(first_crash)
