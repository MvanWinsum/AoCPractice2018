import numpy
serial = 3999

def power(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += serial
    power *= rack
    return (power // 100 % 10) - 5

grid = numpy.fromfunction(power, (300, 300))
highest_power = 0
for width in range(3, 40):
    windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
    maximum = int(windows.max())
    location = numpy.where(windows == maximum)
    if maximum > highest_power:
        highest_power = maximum
    print(width, maximum, location[0][0] + 1, location[1][0] + 1)

print(highest_power)