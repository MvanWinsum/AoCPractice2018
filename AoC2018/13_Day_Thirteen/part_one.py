from collections import deque
import collections
import pprint

pp = pprint.PrettyPrinter(indent=4)
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
        if grid_index not in curves:
            curves[grid_index] = {}
        curves[grid_index][curve] = '/'
    for curve in find(grid_line, '\\'):
        if grid_index not in curves:
            curves[grid_index] = {}
        curves[grid_index][curve] = '\\'
    # Parse Intersections
    for intersection in find(grid_line, '+'):
        if grid_index not in intersections:
            intersections[grid_index] = {}
        intersections[grid_index][intersection] = '+'
    # Parse Carts
    for cart in find(grid_line, '>'):
        carts[grid_index] = {cart: ['R', deque(['L', 'S', 'R'])]}
    for cart in find(grid_line, '<'):
        carts[grid_index] = {cart: ['L', deque(['L', 'S', 'R'])]}
    for cart in find(grid_line, '^'):
        carts[grid_index] = {cart: ['U', deque(['L', 'S', 'R'])]}
    for cart in find(grid_line, 'v'):
        carts[grid_index] = {cart: ['D', deque(['L', 'S', 'R'])]}


def sort_carts():
    global carts
    carts = collections.OrderedDict(sorted(carts.items()))


def parse_grid():
    index = 0
    for line in grid:
        parse_grid_line(line, index)
        index += 1
    sort_carts()


def adjust_movement_curve(cart, curve):
    new_cart = ['', cart[1]]
    if curve == '/':
        if cart[0] == 'R':
            new_cart[0] = 'U'
        if cart[0] == 'D':
            new_cart[0] = 'L'
        if cart[0] == 'U':
            new_cart[0] = 'R'
        if cart[0] == 'L':
            new_cart[0] = 'D'
    else:
        if cart[0] == 'R':
            new_cart[0] = 'D'
        if cart[0] == 'D':
            new_cart[0] = 'R'
        if cart[0] == 'U':
            new_cart[0] = 'L'
        if cart[0] == 'L':
            new_cart[0] = 'U'
    return new_cart


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
    queue.rotate(-1)
    cart[1] = queue
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
            new_y, new_x = get_new_cart_coordinates(carts[y][x], y, x)
            if new_y in curves and new_x in curves[new_y]:
                new_cart = adjust_movement_curve(cart, curves[new_y][new_x])
                carts[y][x] = new_cart
            if new_y in intersections and new_x in intersections[new_y]:
                carts[y][x] = adjust_movement_intersection(cart)
            if new_y in ticked_carts and new_x in ticked_carts[new_y]:
                first_crash = str(new_x) + ',' + str(new_y)
                return
            if new_y not in ticked_carts:
                ticked_carts[new_y] = {}
            ticked_carts[new_y][new_x] = carts[y][x]
    carts = ticked_carts


parse_grid()
pp.pprint(carts)
while len(first_crash) == 0:
    run_tick()
    sort_carts()
pp.pprint(first_crash)
